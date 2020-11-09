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
        list_id = search.database_search_and_find(request.POST.get('search'))
        if list_id:
            message = "Vous pouvez remplacer l'aliment par : "
        else:
            message = "Nous n'avons pas trouvé d'aliment de subsitution."
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
