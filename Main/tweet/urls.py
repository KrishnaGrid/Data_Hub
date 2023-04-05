from django.contrib import admin
from django.urls import path,include
from . import views
from .views import tweets_view

urlpatterns = [
    path('', views.tweets_view,name='tweet'),
]
# show_tweets/