from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.register, name = "register"),
    path('register/', views.register, name = "register"),
    path('home/', views.home, name = "home"),
    path('logout/', views.user_logout, name = "logout"),
    path('login/', views.user_login, name = "login")

]