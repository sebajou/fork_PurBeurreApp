from django.contrib.auth.forms import UserCreationForm
from database_handler_app.models import MyUsers, Allergen, Diet
from django import forms


class SignUpForm(UserCreationForm, forms.Form):

    # Alery from many to many field. Several alergy choice possible.
    alergy = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Allergen.objects.all()
    )

    # Diet from many to many field. Only one choice possible.
    diet_type = forms.ModelChoiceField(
        widget=forms.RadioSelect,
        queryset=Diet.objects.all()
    )

    class Meta:
        model = MyUsers
        fields = ('username', 'first_name', 'last_name', 'email', 'diet_type',
                  'alergy', 'password1', 'password2', 'image_profile')


