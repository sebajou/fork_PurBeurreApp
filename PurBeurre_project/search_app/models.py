from django.db import models


class Alergen(models.Model):
    alergen_name = models.CharField(max_length=200, unique=True)


class Food_list(models.Model):
    food_name = models.CharField(max_length=200, unique=True, null=False)
    category = models.CharField(max_length=200, unique=False, null=False)
    scora_nova_group = models.IntegerField(unique=False, null=True)
    nutri_score_grad = models.CharField(max_length=1, unique=False, null=True)
    food_url = models.TextField(unique=False, null=True)
    alergen_list = models.ManyToManyField(Alergen, related_name='food_list', blank=True)


class Users(models.Model):
    first_name = models.CharField(max_length=200, unique=False, null=False)
    last_name = models.CharField(max_length=200, unique=False, null=False)
    email = models.EmailField(max_length=254, unique=True, null=False)
    password = models.CharField(max_length=256, unique=False, null=False)
    diet_type = models.CharField(max_length=200, unique=False, null=True)
    search_food = models.ManyToManyField(Food_list, related_name='users', blank=True)
    alergy = models.ManyToManyField(Alergen, related_name='users', blank=True)
