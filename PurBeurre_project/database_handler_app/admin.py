from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUsers

admin.site.register(MyUsers, UserAdmin)