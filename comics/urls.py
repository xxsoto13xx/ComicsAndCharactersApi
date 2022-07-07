from django.urls import path
from . import views

urlpatterns = [path('searchComics/comics/',
                    views.comics, name='comics'), ]
