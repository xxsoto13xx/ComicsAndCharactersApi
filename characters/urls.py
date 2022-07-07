from django.urls import path
from . import views

urlpatterns = [path('searchComics/characters/',
                    views.characters, name='characters'), ]
