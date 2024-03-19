from django import forms
from django.contrib.auth.models import User
from wad.models import UserProfile,Recipe, starRating
from django.core.exceptions import ValidationError



#need form for recipes to collect information submitted by users adding recipes
#also need form for users leaving ratings, should link to the starRating model as that is where ratings are stored

        
class RecipeForm(forms.ModelForm):
    name = forms.CharField(
        max_length=Recipe.NAME_MAX_LENGTH,
        help_text="Please enter the Recipe name.",
        label="Recipe Name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter Recipe Name'})
    )
    cuisine = forms.ChoiceField(
        choices=Recipe.CUISINE_CHOICES,
        help_text="Please select a cuisine.",
        label="Cuisine"
    )
    ingredients = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter ingredients'}),
        help_text="Please enter the ingredients.",
        label="Ingredients"
    )
    instructions = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter instructions'}),
        help_text="Please enter the instructions.",
        label="Instructions"
    )
    image = forms.ImageField(
        help_text="Please upload a picture of your recipe.",
        label="Add Photo"
    )

    class Meta:
        model = Recipe
        fields = ('name', 'cuisine', 'ingredients', 'instructions', 'image',)
        
        

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    forename = forms.CharField(max_length=128)
    surname = forms.CharField(max_length=128)
    dateOfBirth = forms.DateField(label="Date of Birth", required=True)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'forename', 'surname', 'dateOfBirth', 'email', 'password', 'confirm_password')
        labels = {
            'dateOfBirth': 'Date of Birth',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)

class RatingForm(forms.ModelForm):
    class Meta:
        model = starRating
        fields = ['rating', 'recipeID']

    def __init__(self, *args, **kwargs):
        super(RatingForm, self).__init__(*args, **kwargs)
        self.fields['recipe'].widget = forms.HiddenInput() 
