# Generated by Django 2.2.28 on 2024-03-07 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wad', '0003_recipe_avgstarrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='avgStarRating',
        ),
    ]
