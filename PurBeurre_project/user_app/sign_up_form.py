from django.contrib.auth.forms import UserCreationForm
from database_handler_app.models import MyUsers, Alergen
from django import forms


class SignUpForm(UserCreationForm, forms.Form):

    alergy = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Alergen.objects.all()
    )

    class Meta:
        model = MyUsers
        fields = ('username', 'first_name', 'last_name', 'email', 'diet_type', 'alergy', 'password1', 'password2',)


class AlergyForm(forms.ModelForm):

    class Meta:
        model = Alergen
        fields = ('alergen_name', )

