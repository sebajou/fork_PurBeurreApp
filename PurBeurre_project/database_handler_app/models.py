from django.db import models
from django.contrib.auth.models import AbstractUser


class Alergen(models.Model):
    alergen_name = models.CharField(max_length=200, unique=True)


class FoodList(models.Model):
    food_name = models.CharField(max_length=200, unique=True, null=False)
    category = models.CharField(max_length=200, unique=False, null=False)
    scora_nova_group = models.IntegerField(unique=False, null=True)
    nutri_score_grad = models.CharField(max_length=1, unique=False, null=True)
    food_url = models.TextField(unique=False, null=True)
    image_src = models.TextField(unique=False, null=True)
    alergen_list = models.ManyToManyField(Alergen, related_name='food_list', blank=True)


class MyUsers(AbstractUser):
    diet_type = models.CharField(max_length=200, unique=False, null=True)
    search_food = models.ManyToManyField(FoodList, related_name='users', blank=True)
    alergy = models.ManyToManyField(Alergen, related_name='users', blank=True)


class Favorites(models.Model):
    favorites_list = models.ManyToManyField(MyUsers, related_name='favorites', blank=True)
    id_food_list = models.ForeignKey(FoodList, on_delete=models.DO_NOTHING)