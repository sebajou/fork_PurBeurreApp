from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from request_api_app.search_engine import FindSubstitute
from request_api_app.alergen_diet import IsFood
from database_handler_app.models import MyUsers, Favorites, FoodList, Allergen, Diet
import json


def index(request):
    """Main page"""
    template = loader.get_template('database_handler_app/index.html')
    return HttpResponse(template.render(request=request))


def search_results(request):
    """
    Allow the user to obtain search results from text POST.
    Input: POST text with food name.
    Process:
        foods_ids = search_engine.FindSubstitute.database_search_and_find(input)
        dict_healthy_substitute = search_engine.FindSubstitute.healthy_substitute(foods_ids)
    Output: sort healthy foods substitute search results from database.
    Use search_engine module functionalities.
    """
    if request.method == 'POST':
        # Instanciation of class with method to find substitute and to bool allergen and diet
        search = FindSubstitute()
        is_bool = IsFood()
        # Post data from search field
        search_posted = request.POST.get('search')
        # Post bool data to know is the search must exclude user's allergen and by adequate with user's diet
        diet_posted = request.POST.get('diet')
        print("diet_posted => ", diet_posted)
        allergen_posted = request.POST.get('allergen')
        print("allergen_posted => ", allergen_posted)
        # List of id of substitute from Post data with a method
        list_id = search.database_search_and_find(search_posted)
        # Create message specific for the type of value enter in search field
        message = ""
        dict_healthy_substitute = {}
        for element_id in list_id:
            if element_id == "-µ-empty-µ-":
                message = "Vous n'avez rien rentrer dans le champs de recherche."
                dict_healthy_substitute = {}
            elif element_id == '-µ-absurd-µ-':
                message = "Nous n'avons pas trouvé d'aliment de subsitution."
                dict_healthy_substitute = {}
            else:
                message = "Vous pouvez remplacer l'aliment par : "
                # Obtain dictionnary with useful data for substitute from list of substitue id
                dict_healthy_substitute = search.healthy_substitute(list_id[0]['id'])

        dict_healthy_substitute = list(dict_healthy_substitute)
        # Obtain list of allergen and diet of the current user.
        # Remove food with user's allergen from dict_healthy_substitute.
        if allergen_posted:
            dict_allergen_of_user = Allergen.objects.filter(myusers__id=request.user.id).values()
            list_allergen_of_user = []
            for allergen in dict_allergen_of_user:
                list_allergen_of_user.append(allergen['allergen_name'])
            print("list_allergen_of_user => ", list_allergen_of_user)
            i = 0
            for food_id in dict_healthy_substitute:
                print("food_id['id'] => ", food_id['id'])
                is_allergen = is_bool.is_allergen(allergen_list=list_allergen_of_user, id_food=food_id['id'])
                print('is_allergen => ', is_allergen)
                if is_allergen:
                    del dict_healthy_substitute[i]
                i += 1
        # Remove food not adequate with user diet from list_id.
        if diet_posted:
            diet_of_user = Diet.objects.filter(myusers__id=request.user.id).values()
            diet_of_user = diet_of_user[0]['diet_name']
            print("diet_of_user => ", diet_of_user)
            j = 0
            for food_id in dict_healthy_substitute:
                is_diet = is_bool.is_diet(diet_type=diet_of_user[0], id_food=food_id['id'])
                if not is_diet:
                    del dict_healthy_substitute[j]
                j += 1

        return render(request, 'database_handler_app/search_results.html',
                      {'list_id': list_id, 'message': message, 'dict_healthy_substitute': dict_healthy_substitute[:6]})


def is_favorite(request):
    """Allow user to record favorites food in database. Reroute on favorites list page."""
    if request.method == 'POST':
        # Input from user food button selection.
        id_favorite_food = request.POST.get('favorite_substitute_id')
        print('id_favorite_food => ', id_favorite_food)
        # Determined the current user.
        current_user = request.user
        print('current_user => ', current_user)
        # Add User favorite choice in database through many to many relationship.
        qs_user = MyUsers.objects.get(username=current_user)
        print('qs_user => ', qs_user)
        if Favorites.objects.filter(id_food_list=id_favorite_food):
            qs_favorite = Favorites.objects.get(id_food_list=id_favorite_food)
        else:
            fav = Favorites(id_food_list_id=id_favorite_food)
            fav.save()
            qs_favorite = Favorites.objects.get(id_food_list=id_favorite_food)
        print('qs_favorite => ', qs_favorite)
        qs_favorite.favorites_list.add(qs_user)
        return redirect('my_foods')


def legal_mention(request):
    """Legal mention page. """
    message = "NOTICE LÉGALE - CONDITIONS D'UTILISATION"
    return render(request, 'database_handler_app/legal_mention.html', {'message': message})


def my_foods(request):
    """Route for user's favorites list."""
    if request.user.is_authenticated:
        # Obtain all favorites food record by a user from many to many relationship
        list_object_favorites_of_user = Favorites.objects.filter(favorites_list__id=request.user.id)
        print("username => ", request.user.username)
        # Obtain id of this favorites food
        list_favorites_id_of_user = []
        for object_favorites_of_user in list_object_favorites_of_user:
            list_favorites_id_of_user.append(object_favorites_of_user.id_food_list_id)
        # Obtain dictionary from food id in foodlist
        list_dict_favorites_of_user = []
        for favorites_id_of_user in list_favorites_id_of_user:
            qs_dict_favortites_of_user = FoodList.objects.filter(id=favorites_id_of_user)
            qs_dict_favortites_of_user = qs_dict_favortites_of_user.values()
            for dict_favortites_of_user in qs_dict_favortites_of_user:
                list_dict_favorites_of_user.append(dict_favortites_of_user)
        if list_dict_favorites_of_user:
            message = "Votre liste de produit favories : "
        else:
            message = "Vous n'avez pas de favories enregistré. "

        return render(request, 'database_handler_app/my_foods.html',
                      {'list_dict_favorites_of_user': list_dict_favorites_of_user, 'message': message})
    else:
        print('not log')
        return render(request, 'registration/login.html')


def food_page(request):
    """
    Identity food page.
    From food id post from button display all necessary information about this food.
    """
    if request.method == 'POST':
        # Obtain food id
        id_food = request.POST.get('id_food')
        print("id_food => ", id_food)
        # From food id fill dictionary for all necessary food's information from database.
        dict_food = {}
        dict_nutriments_100g = {}
        str_nutriments_100g = ""
        if FoodList.objects.filter(id=id_food):
            qs_dict_food = FoodList.objects.filter(id=id_food)
            dict_food = qs_dict_food.values()
            for ele in dict_food:
                str_nutriments_100g = ele['nutriments_100g'].replace("\'", "\"")
            dict_nutriments_100g = json.loads(str_nutriments_100g)
            message = "Nous avons une page pour cette aliments. "
        else:
            message = "Nous n'avons pas de page pour cette aliments. "

        return render(request, 'database_handler_app/food_page.html',
                      {'dict_food': dict_food, 'dict_nutriments_100g': dict_nutriments_100g, 'message': message})
