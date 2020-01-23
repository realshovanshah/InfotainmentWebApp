from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Show
# Create your views here.


def home(request):
	return render(request=request, template_name="pages/home.html", context={"shows": Show.objects.all})

def upload(request):
    if request.method == 'POST':
        shows_name = request.POST['shows_name']
        shows_type = request.POST['shows_type']
        shows_description = request.POST['shows_description']
        upload = Show(shows_name = shows_name, shows_type = shows_type, shows_description = shows_description)
        upload.save()
        return HttpResponse('Thank You For Uploading')
    else:   
        return render(request,'pages/upload.html')