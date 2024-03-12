from django.urls import path
from wad.views import (
    home, RegisterView, UserLoginView, UserLogoutView, CuisineView,
    ItalianView, ChineseView, ThaiView, IndianView, AddRecipeView,
    ViewRecipeView, MyRecipesView, rate_recipe
)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'wad'

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('cuisine/', CuisineView.as_view(), name='cuisine'),
    path('italian/', ItalianView.as_view(), name='italian'),
    path('chinese/', ChineseView.as_view(), name='chinese'),
    path('thai/', ThaiView.as_view(), name='thai'),
    path('indian/', IndianView.as_view(), name='indian'), 
    path('addrecipe/', AddRecipeView.as_view(), name='addrecipe'),
    path('myrecipes/', MyRecipesView.as_view(), name='myrecipes'),
    path('viewrecipe/<str:cuisine_name>/<slug:recipe_name_slug>/', 
         ViewRecipeView.as_view(), name='view_recipe'),
    path('raterecipe/', rate_recipe, name='raterecipe'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
