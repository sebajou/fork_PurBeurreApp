# Generated by Django 3.1.1 on 2020-12-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_handler_app', '0003_auto_20201207_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodlist',
            name='allergen_list',
            field=models.ManyToManyField(null=True, to='database_handler_app.Allergen'),
        ),
        migrations.AlterField(
            model_name='myusers',
            name='alergy',
            field=models.ManyToManyField(to='database_handler_app.Allergen'),
        ),
    ]
