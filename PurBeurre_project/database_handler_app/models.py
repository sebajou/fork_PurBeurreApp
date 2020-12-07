from django.db import models
from django.contrib.auth.models import AbstractUser


class Allergen(models.Model):
    allergen_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.allergen_name


class Diet(models.Model):
    diet_name = models.CharField(max_length=200, unique=False, null=True)

    def __str__(self):
        return self.diet_name


class FoodList(models.Model):
    food_name = models.CharField(max_length=200, unique=True, null=False)
    category = models.CharField(max_length=200, unique=False, null=False)
    scora_nova_group = models.IntegerField(unique=False, null=True)
    nutri_score_grad = models.CharField(max_length=1, unique=False, null=True)
    food_url = models.TextField(unique=False, null=True)
    image_src = models.TextField(unique=False, null=True)
    nutriments_100g = models.TextField(unique=False, null=True)
    allergen_list = models.ManyToManyField(Allergen)


class MyUsers(AbstractUser, models.Model):
    diet_type = models.ManyToManyField(Diet)
    search_food = models.ManyToManyField(FoodList)
    alergy = models.ManyToManyField(Allergen)
    image_profile = models .ImageField(upload_to='profile_image/', null=True, blank=True,
                                       default='elephant.jpeg')


class Favorites(models.Model):
    favorites_list = models.ManyToManyField(MyUsers)
    id_food_list = models.ForeignKey(FoodList, on_delete=models.DO_NOTHING)
