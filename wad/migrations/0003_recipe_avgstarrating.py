# Generated by Django 2.2.28 on 2024-03-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wad', '0002_auto_20240305_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='avgStarRating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]