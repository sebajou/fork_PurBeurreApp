from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from database_handler_app.models import MyUsers, Alergen, Diet
from user_app.sign_up_form import SignUpForm
from django.views.generic import ListView


def user_form(request):
    if request.method == 'POST':
        # Form for sign up from class in sign_up_form.py module
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # authentification and login
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # special treatment of data alergy and diet which from many to many field
            qs_username = MyUsers.objects.get(username=username)
            choose_diet = request.POST.get('diet_type')
            print('choose_diet: ', choose_diet)
            qs_diet = Diet.objects.get(id=choose_diet)
            qs_username.diet_type.add(qs_diet)
            choose_alergen = request.POST.getlist('alergy')
            for id_alergen in choose_alergen:
                qs_alergen = Alergen.objects.get(id=id_alergen)
                qs_username.alergy.add(qs_alergen)

            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def view_profile(request, id=None):
    print("maybe")
    if request.user.is_authenticated:
        user = request.user.get_profile()

        # user = MyUsers.objects.all()

        print("yes")
    else:
        user = request.user
        print("no")
    return render(request, 'registration/profile.html')

"""
class ProfileViewsList(ListView):
    model = MyUsers
    template_name = "myusers_list.html"

    # queryset = MyUsers.objects.all()
    queryset = MyUsers.objects.filter(is_active=True)
    context_object_name = 'profile_list'
"""
