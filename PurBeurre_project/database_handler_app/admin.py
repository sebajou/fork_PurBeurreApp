from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUsers, Allergen, Diet, FoodList, Favorites


admin.site.register(Allergen, Diet, FoodList, Favorites)
admin.site.register(MyUsers, UserAdmin)
