from django import forms
from django.contrib.auth.models import User
from wad.models import UserProfile,Recipe, starRating
from django.core.exceptions import ValidationError
 
class RecipeForm(forms.ModelForm):
    name = forms.CharField(
        max_length=Recipe.NAME_MAX_LENGTH,
        label="Recipe Name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter Recipe Name'})
    )
    cuisine = forms.ChoiceField(
        choices=Recipe.CUISINE_CHOICES,
        label="Cuisine"
    )
    ingredients = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter ingredients'}),
        label="Ingredients"
    )
    instructions = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter instructions'}),
        label="Instructions"
    )
    image = forms.ImageField(
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
    dateOfBirth = forms.DateField(label="Date of Birth  (YYYY-MM-DD)", input_formats=['%Y-%m-%d'])
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
        self.fields['recipeID'].widget = forms.HiddenInput()


