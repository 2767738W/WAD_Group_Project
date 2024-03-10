from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.template.defaultfilters import slugify
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
        return self.starrating_set.aggregate(Avg('rating'))['rating__avg'] or 0

    def save(self, *args, **kwargs):
        # Update the average star rating whenever the recipe is saved
        if not self.slug:
            self.slug = slugify(self.name)
        self.avgStarRating = self.avg_star_rating()  # Update the average star rating
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

    
    

