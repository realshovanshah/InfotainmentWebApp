from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views

# app_name = "main"

urlpatterns = [
    path('feedback/', views.comment, name='feedback')
]
