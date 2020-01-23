from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Show
from django.db.models import Q
# Create your views here.


def home(request):
	# return render(request=request, template_name="pages/home.html", context={"shows": Show.objects.all})
    show = Show.objects.all()
    if request.GET:
        query = request.GET['q']
        show = get_data_queryset(str(query))
    return render(request, "pages/home.html", {"shows": show})

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

def show_list(request):
    show = Show.objects.all()
    if request.GET:
        query = request.GET['q']
        show = get_data_queryset(str(query))
    return render(request, "pages/home.html", {"shows": show})


def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        shows= Show.objects.filter(
            Q(shows_name__icontains=q) |
            Q(shows_type__icontains=q) |
            Q(shows_description__icontains=q)
        )
    for show in shows:
        queryset.append(show)
    return list(set(queryset))
