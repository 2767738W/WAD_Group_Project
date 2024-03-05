from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserProfile(models.Model):
    NAME_MAX_LENGTH = 128

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forename = models.CharField(max_length=NAME_MAX_LENGTH)
    surname = models.CharField(max_length=NAME_MAX_LENGTH)
    dateOfBirth = models.DateField()
    email = models.EmailField()

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username
   
   
   
class Recipe(models.Model):
    RECIPE_MAX_LENGTH = 1024
    NAME_MAX_LENGTH = 128
    
    CUISINE_CHOICES = [
        ('italian', 'Italian'),
        ('chinese', 'Chinese'),
        ('thai', 'Thai'),
        ('indian', 'Indian'),
    ]
    
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    cuisine = models.CharField(max_length=7, choices=CUISINE_CHOICES)
    ingredients = models.TextField(max_length = RECIPE_MAX_LENGTH)
    instructions = models.TextField(max_length = RECIPE_MAX_LENGTH)
    avgStarRating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    image = models.ImageField(upload_to=user_directory_path)
    
    def update_avg_star_rating(self):
        avg_rating = self.starrating_set.aggregate(Avg('rating'))['rating__avg']

        self.avgStarRating = avg_rating if avg_rating is not None else 0
        self.save()
    
    
    
    
    
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

    
    

