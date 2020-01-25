from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Show
from .forms import UploadShows
from django.db.models import Q
from .forms import UploadShows
from django.contrib import messages

# Create your views here.


def home(request):
	# return render(request=request, template_name="pages/home.html", context={"shows": Show.objects.all})
    show = Show.objects.all()
    if request.GET:
        query = request.GET['q']
        show = get_data_queryset(str(query))
    return render(request, 'home/home.html', {'shows': show})

def upload(request):
    if request.method == 'POST':
       form = UploadShows(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('main:home')
    form = UploadShows()
    return render (request,'home/upload.html',{'form':form})


def show_list(request):
    show = Show.objects.all()
    if request.GET:
        query = request.GET['q']
        show = get_data_queryset(str(query))
    return render(request, "home/home.html", {"shows": show})


def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        shows= Show.objects.filter(
            Q(shows_Name__icontains=q)
        )
    for show in shows:
        queryset.append(show)
    return list(set(queryset))

def delete_show(request, pk):
    show = Show.objects.get(pk=pk)
    show.delete()
    return redirect('main:home')

def update(request, show_id):
    show_obj = Show.objects.get(pk=show_id)
    post = request.POST or None
    file = request.FILES or None
    show_form = UploadShows(post,file,instance=
        show_obj)
    if show_form.is_valid():
        show_form.save()
        messages.success(request, f'Post updated.')
        return redirect('main:home')
    context = {
        'show_form': show_form,
    }
    #if admin
    return render(request, 'home/update.html', context)
