from django.urls import path
from wad import views

app_name = 'wad'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('cuisine/', views.cuisine, name='cuisine'),
    path('italian/', views.italian, name='italian'),
    path('chinese/', views.chinese, name='chinese'),
    path('thai/', views.thai, name='thai'),
    path('indian/', views.indian, name='indian'), 
    path('addrecipe/', views.addrecipe, name='addrecipe'),
    path('viewrecipe/', views.viewrecipe, name='viewrecipe'),
    path('myrecipes/', views.myrecipes, name='myrecipes'),
    path('viewrecipe/<slug:recipe_name_slug>/',
         views.viewrecipe, name='view_recipe'),
]
