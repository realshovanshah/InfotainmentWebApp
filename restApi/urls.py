from django.urls import path
from . import views

app_name = "restApi"
urlpatterns = [
	path('restful/',views.api_data, name='api_data'),
	path('restful/<int:pk>/',views.api_get_data, name='api_get_data'),
	path('restful/<int:PAGENO>/<int:SIZE>',views.api_pagination,name="api_pagination"),
	path('restful/add/',views.api_add_data, name = "api_add_data"),
	path('restful/update/<int:pk>/',views.api_update_data, name = "api_update_data"),
]