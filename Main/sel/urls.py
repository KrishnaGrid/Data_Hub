from django.contrib import admin
from django.urls import path,include
from . import views
from .views import search_movie

urlpatterns = [
    path('', views.search_movie),
]
