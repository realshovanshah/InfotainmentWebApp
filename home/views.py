from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Show
# Create your views here.


def home(request):
	return render(request=request, template_name="pages/home.html", context={"shows": Show.objects.all})
