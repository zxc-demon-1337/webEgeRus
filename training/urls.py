from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.training_home, name='training_home')
]