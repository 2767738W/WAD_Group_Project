from django import forms
from django.contrib.auth.models import User
from wad.models import UserProfile
from wad.models import Recipe


#need form for recipes to collect information submitted by users adding recipes
#also need form for users leaving ratings, should link to the starRating model as that is where ratings are stored

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)