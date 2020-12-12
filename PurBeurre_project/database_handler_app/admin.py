from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUsers, Allergen, Diet, FoodList, Favorites


admin.site.register(Allergen)
admin.site.register(Diet)
admin.site.register(FoodList)
admin.site.register(Favorites)
admin.site.register(MyUsers, UserAdmin)
