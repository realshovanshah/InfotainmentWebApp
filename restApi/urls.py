from django.urls import path
from . import views

app_name = "restApi"
urlpatterns = [
	path('restful/',views.api_data, name='api_data'),
	path('restful/<int:pk>/',views.edited_data, name='edited_data'),
]