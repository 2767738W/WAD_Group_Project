from django.urls import path
from wad import views

app_name = 'wad'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('cuisine/', views.cuisine, name='cuisine'),
    path('cuisine/<slug:cuisine_name_slug>/', views.cuisine_detail, name='cuisine_detail'),
    path('cuisine/<slug:cuisine_name_slug>/addrecipe/', views.add_recipe, name='add_recipe'),
    path('cuisine/<slug:cuisine_name_slug>/viewrecipe/', views.view_recipes, name='view_recipes'),
]
