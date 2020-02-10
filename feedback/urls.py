from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views

app_name = "feedback"

urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    path('feedback/<int:pk>', views.delete_feedback, name='feedback'),
    path('details/', views.show_feedback, name='details')
]
