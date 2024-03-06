from django import forms
from django.contrib.auth.models import User
from wad.models import UserProfile
from wad.models import Recipe


#need form for recipes to collect information submitted by users adding recipes
#also need form for users leaving ratings, should link to the starRating model as that is where ratings are stored
class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length = Recipe.NAME_MAX_LENGTH, help_text = "Please enter the Recipe name. ")
    cuisine = forms.ChoiceField(choices = Recipe.CUISINE_CHOICES, help_text = "Please select a cuisine. ")
    ingredients = forms.CharField(widget = forms.Textarea, help_text = "Please enter the ingredients. ")
    instructions = forms.CharField(widget = forms.Textarea, help_text = "Please enter the instructions. ")
    image = forms.ImageField(help_text = "Please upload a picture of your recipe. ")

    class Meta:
        model = Recipe
        fields = ('name', 'cuisine', 'ingredients', 'instructions', 'image',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)