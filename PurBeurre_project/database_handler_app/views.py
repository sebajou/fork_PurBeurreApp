from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect
from request_api_app.search_engine import FindSubstitute
from database_handler_app.models import MyUsers, Favorites, FoodList
import json


def index(request):
    template = loader.get_template('database_handler_app/index.html')
    return HttpResponse(template.render(request=request))


def search_results(request):
    if request.method == 'POST':
        # Instanciation of class with method to find substitute
        search = FindSubstitute()
        # Post data from search field
        search_posted = request.POST.get('search')
        # List of id of substitute from Post data with a method
        list_id = search.database_search_and_find(search_posted)
        # Create message specifique for the type of value enter in search field
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
        return render(request, 'database_handler_app/search_results.html',
                      {'list_id': list_id, 'message': message, 'dict_healthy_substitute': dict_healthy_substitute})


def is_favorite(request):
    if request.method == 'POST':
        # id_favorite_food = form.cleaned_data.get('id_favorite_food')
        # id_favorite_food = request.POST.get('id_favorite_food', None)
        id_favorite_food = request.POST.get('favorite_substitute_id')
        print('id_favorite_food => ', id_favorite_food)
        current_user = request.user
        print('current_user => ', current_user)
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
    message = "Hello World !"
    """template = loader.get_template('database_handler_app/search_results.html')
    return HttpResponse(template.render(request=request))"""
    return render(request, 'database_handler_app/legal_mention.html', {'message': message})


def my_foods(request):
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
    if request.method == 'POST':
        id_food = request.POST.get('id_food')
        print("id_food => ", id_food)
        dict_food = {}
        dict_nutriments_100g = {}
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
