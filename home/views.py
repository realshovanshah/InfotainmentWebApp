from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Show
from django.db.models import Q


#function for homepage and listing the shows.
def home(request):
    show = Show.objects.all()
    if request.GET:
        query = request.GET['q']
        show = get_data_queryset(str(query))
    return render(request, "pages/home.html", {"shows": show})


#function for uploading.
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


#funtion for searching specific movies or series.
def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:  #filters show_name, show_type and show_description that matvhes the keywords while searching.
        shows= Show.objects.filter(
            Q(shows_name__icontains=q) |
            Q(shows_type__icontains=q) |
            Q(shows_description__icontains=q)
        )
    for show in shows:  #provides us with shows after searching.
        queryset.append(show)
    return list(set(queryset))
