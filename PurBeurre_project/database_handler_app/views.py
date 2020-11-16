from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect
from request_api_app.search_engine import FindSubstitute
from database_handler_app.models import MyUsers, Favorites


def index(request):
    template = loader.get_template('database_handler_app/index.html')
    return HttpResponse(template.render(request=request))


def search_results(request):
    if request.method == 'POST':
        search = FindSubstitute()
        search_posted = request.POST.get('search')
        list_id = search.database_search_and_find(search_posted)
        for element_id in list_id:
            if element_id == "-µ-empty-µ-":
                message = "Vous n'avez rien rentrer dans le champs de recherche."
                dict_healthy_substitute = {}
            elif element_id == '-µ-absurd-µ-':
                message = "Nous n'avons pas trouvé d'aliment de subsitution."
                dict_healthy_substitute = {}
            else:
                message = "Vous pouvez remplacer l'aliment par : "
                dict_healthy_substitute = search.healthy_substitute(list_id[0]['id'])
        return render(request, 'database_handler_app/search_results.html',
                      {'list_id': list_id, 'message': message, 'dict_healthy_substitute': dict_healthy_substitute})


def ajax_is_favorite(request):
    data = {'success': False}
    if request.method == 'POST':
        id_favorite_food = int(request.POST.get('id_favorite_food'))
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
        data['success'] = True
    return JsonResponse(data)


def legal_mention(request):
    message = "Hello World !"
    """template = loader.get_template('database_handler_app/search_results.html')
    return HttpResponse(template.render(request=request))"""
    return render(request, 'database_handler_app/legal_mention.html', {'message': message})


def my_foods(request):
    message = "Hello World !"
    """template = loader.get_template('database_handler_app/search_results.html')
    return HttpResponse(template.render(request=request))"""
    return render(request, 'database_handler_app/my_foods.html', {'message': message})
