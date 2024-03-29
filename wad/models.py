from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from uuid import uuid4


def user_directory_path(instance, filename):
    _, ext = os.path.splitext(filename)
    
    unique_filename = f"{uuid4()}{ext}"

    return unique_filename


class UserProfile(models.Model):
    NAME_MAX_LENGTH = 128

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forename = models.CharField(max_length=NAME_MAX_LENGTH)
    surname = models.CharField(max_length=NAME_MAX_LENGTH)
    dateOfBirth = models.DateField(null=True, blank=True)
    email = models.EmailField()

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username
   
   
   
class Recipe(models.Model):
    RECIPE_MAX_LENGTH = 8192
    NAME_MAX_LENGTH = 128
    
    CUISINE_CHOICES = [
        ('italian', 'Italian'),
        ('chinese', 'Chinese'),
        ('thai', 'Thai'),
        ('indian', 'Indian'),
    ]
    
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    cuisine = models.CharField(max_length=7, choices=CUISINE_CHOICES)
    ingredients = models.TextField(max_length = RECIPE_MAX_LENGTH)
    instructions = models.TextField(max_length = RECIPE_MAX_LENGTH)
    image = models.ImageField(upload_to=user_directory_path)
    slug = models.SlugField(unique=True)

    def avg_star_rating(self):
        avg_rating = self.starrating_set.aggregate(avg_rating=Avg('rating'))['avg_rating']
        if avg_rating is None:
            return "Not rated yet"
        else: 
            return avg_rating

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
class starRating(models.Model):
    userID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    recipeID = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default = 0,
        validators = [
            MaxValueValidator(limit_value=5),
            MinValueValidator(limit_value=0)
        ]
    )
    

    def __str__(self):
        return f"{self.userID} - {self.recipeID} - {self.rating}"

@receiver(post_save, sender=starRating)
def update_recipe_avg_rating(sender, instance, created, **kwargs):
    if created:
        avg_rating = instance.recipeID.starrating_set.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0
        instance.recipeID.avg_star_rating = avg_rating
        instance.recipeID.save()

    
    

