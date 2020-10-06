from django.db import models
from django.contrib.auth.models import AbstractUser


class Alergen(models.Model):
    alergen_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.alergen_name


class FoodList(models.Model):
    food_name = models.CharField(max_length=200, unique=True, null=False)
    category = models.CharField(max_length=200, unique=False, null=False)
    scora_nova_group = models.IntegerField(unique=False, null=True)
    nutri_score_grad = models.CharField(max_length=1, unique=False, null=True)
    food_url = models.TextField(unique=False, null=True)
    image_src = models.TextField(unique=False, null=True)
    alergen_list = models.ManyToManyField(Alergen)


class MyUsers(AbstractUser):
    diet_type = models.CharField(max_length=200, unique=False, null=True)
    search_food = models.ManyToManyField(FoodList)
    alergy = models.ManyToManyField(Alergen)


class Favorites(models.Model):
    favorites_list = models.ManyToManyField(MyUsers)
    id_food_list = models.ForeignKey(FoodList, on_delete=models.DO_NOTHING)