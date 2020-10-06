# Generated by Django 3.1.1 on 2020-10-06 13:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_handler_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='favorites_list',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='foodlist',
            name='alergen_list',
            field=models.ManyToManyField(to='database_handler_app.Alergen'),
        ),
        migrations.AlterField(
            model_name='myusers',
            name='alergy',
            field=models.ManyToManyField(to='database_handler_app.Alergen'),
        ),
        migrations.AlterField(
            model_name='myusers',
            name='search_food',
            field=models.ManyToManyField(to='database_handler_app.FoodList'),
        ),
    ]
