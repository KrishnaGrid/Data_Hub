from django.contrib import admin
from django.urls import path,include
from .views import movie_and_show_list
from . import views

urlpatterns = [
    path("",views.movie_and_show_list),
]