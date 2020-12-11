from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from database_handler_app.models import MyUsers, Allergen, Diet
from user_app.sign_up_form import SignUpForm


def user_form(request):
    """Sign up form. """
    if request.method == 'POST':
        # Form for sign up from class in sign_up_form.py module
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # authentication and login
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # special treatment of data alergy and diet which from many to many field
            qs_username = MyUsers.objects.get(username=username)
            choose_diet = request.POST.get('diet_type')
            print('choose_diet: ', choose_diet)
            qs_diet = Diet.objects.get(id=choose_diet)
            qs_username.diet_type.add(qs_diet)
            choose_allergen = request.POST.getlist('alergy')
            for id_allergen in choose_allergen:
                qs_allergen = Allergen.objects.get(id=id_allergen)
                qs_username.alergy.add(qs_allergen)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    """Display profile page. """
    if request.user.is_authenticated:
        alergy = Allergen.objects.filter(myusers__id=request.user.id)
        diet_type = Diet.objects.filter(myusers__id=request.user.id)

        return render(request, 'user_app/profile.html', {'alergy': alergy, 'diet_type': diet_type})

    else:
        return render(request, 'registration/login.html')
