# Generated by Django 2.2.28 on 2024-03-19 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wad', '0013_auto_20240319_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='starrating',
            old_name='recipe_id',
            new_name='recipeID',
        ),
    ]
