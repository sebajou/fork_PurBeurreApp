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
        alergen = AlergyForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
        alergen = AlergyForm()
        # diet_types = ["Omnivor", "Vegan", "Vegetarian", "Carnivor", "Cannibal"]
    return render(request, 'registration/signup.html', {'form': form, 'alergen': alergen})


"""@login_required(redirect_field_name='user_login')
def user_myaccount(request):
    fields = MyUsers.get_username(self)
    return render(request, 'registration/profile.html', {'fields': fields})"""


class ProfileViewsList(ListView):
    model = MyUsers
    template_name = "myusers_list.html"

    queryset = MyUsers.objects.all()
    context_object_name = 'profile_list'