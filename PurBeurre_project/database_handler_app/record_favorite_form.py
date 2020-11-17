from django.db import models
from database_handler_app.models import MyUsers, Favorites
from django import forms


class RecordFavoriteForm(forms.Form):
    # favorite_substitute_id = forms.IntegerField(label='favorite_substitute_id', widget=forms.HiddenInput())
    favorite_substitute_id = forms.CharField(label='favorite_substitute_id')

    class Meta:
        model = Favorites
        fields = 'id_food_list'
