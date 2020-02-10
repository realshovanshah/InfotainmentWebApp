from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views

app_name = "feedback"

urlpatterns = [
    path('feedback/<int:pk>', views.feedback, name='feedback'),
    path('delete/<int:pk>', views.delete_feedback, name='delete'),
    path('details/', views.show_feedback, name='details'),
]
