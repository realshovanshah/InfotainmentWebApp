from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
 
app_name= "home"
urlpatterns = [
    # path('', views.home, name = "home"),
    path('home/', views.home, name = "home"),
    path('upload/',views.upload,name = "upload"),
    path("home/<int:pk>/", views.delete_show, name="delete_show"), #slug to delete specified no.
    path("home/update/<int:show_id>/", views.update, name="update"), #slug to delete specified no.

]	
