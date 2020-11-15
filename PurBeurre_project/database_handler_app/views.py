from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from request_api_app.search_engine import FindSubstitute


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
