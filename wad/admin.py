from django.contrib import admin
from wad.models import UserProfile, Recipe, starRating

admin.site.register(UserProfile)
admin.site.register(Recipe)
admin.site.register(starRating)

