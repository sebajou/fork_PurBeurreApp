from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from database_handler_app.models import MyUsers, Alergen
from user_app.sign_up_form import SignUpForm, AlergyForm
from django.views.generic import ListView


def user_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # alergen = AlergyForm(request.POST)
        if form.is_valid():
            form.save()
            # alergen.save()
            username = form.cleaned_data.get('username')
            print('username: ', username)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            choose_alergy = request.POST.getlist('alergy')
            print('choose_alergy: ', choose_alergy)
            qs_username = MyUsers.objects.get(username=username)
            for alergen in choose_alergy:
                qs_alergen = Alergen.objects.get(id=alergen)
                qs_username.alergy.add(qs_alergen)
            for element in form:
                print(element)
            return redirect('index')
    else:
        form = SignUpForm()
        # alergen = AlergyForm()
        # diet_types = ["Omnivor", "Vegan", "Vegetarian", "Carnivor", "Cannibal"]
    # return render(request, 'registration/signup.html', {'form': form, 'alergen': alergen})
    return render(request, 'registration/signup.html', {'form': form})


"""@login_required(redirect_field_name='user_login')
def user_myaccount(request):
    fields = MyUsers.get_username(self)
    return render(request, 'registration/profile.html', {'fields': fields})"""


class ProfileViewsList(ListView):
    model = MyUsers
    template_name = "myusers_list.html"

    # queryset = MyUsers.objects.all()
    queryset = MyUsers.objects.filter(is_active=True)
    context_object_name = 'profile_list'