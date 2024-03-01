from django.urls import path
from wad import views

app_name = 'wad'

urlpatterns = [
    path('', views.home, name='home'),
]
