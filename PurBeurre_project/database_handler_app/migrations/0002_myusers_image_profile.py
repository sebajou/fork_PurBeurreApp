# Generated by Django 3.1.1 on 2020-12-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_handler_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myusers',
            name='image_profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
    ]
