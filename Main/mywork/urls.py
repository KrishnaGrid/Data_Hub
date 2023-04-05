from django.contrib import admin
from django.urls import path,include
from . import views
from .views import movie_and_show_list

urlpatterns = [
    path('', views.movie_and_show_list),
]