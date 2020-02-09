from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Show, Favorite, Recommendation
from .forms import UploadShows
from django.db.models import Q
from .forms import UploadShows, RecommendationForm
from django.contrib import messages

# Create your views here.
def recommendation(request):
        return render(request=request,template_name="home/recommendation.html")

#function for homepage and listing the shows.
def home(request):
    show = Show.objects.all()
    if request.GET:
        query = request.GET['q']
        show = get_data_queryset(str(query))
    return render(request, 'home/home.html', {'shows': show})

 
#function for uploading.
def upload(request):
    if request.method == 'POST':
       form = UploadShows(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('home:home')
    form = UploadShows()
    return render (request,'home/upload.html',{'form':form})


def recommendationDetail(request):
    if request.method == 'POST':
       rform = RecommendationForm(request.POST)
       if rform.is_valid():
           rform.save()
           return redirect('home:home')
    rform = RecommendationForm()
    return render (request,'home/recommendation.html',{'rform':rform})
# def show_list(request):
#     show = Show.objects.all()
#     if request.GET:
#         query = request.GET['q']
#         show = get_data_queryset(str(query))
#     return render(request, "home/home.html", {"shows": show})


#funtion for searching specific movies or series.
def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:  #filters show_name, show_type and show_description that matvhes the keywords while searching.
        shows= Show.objects.filter(
            Q(shows_Name__icontains=q)
        )
    for show in shows:  #provides us with shows after searching.
        queryset.append(show)
    return list(set(queryset))


def delete_show(request, pk):
    show = Show.objects.get(pk=pk)
    show.delete()
    return redirect('home:home')


def delete_fav(request, pk=None):
    fav = Favorite.objects.get(pk=pk)
    fav.delete()
    return redirect('home:favorites')


def update(request, show_id):
    show_obj = Show.objects.get(pk=show_id)
    post = request.POST or None
    file = request.FILES or None
    show_form = UploadShows(post,file,instance=
        show_obj)
    if show_form.is_valid():
        show_form.save()
        messages.success(request, f'Post updated.')
        return redirect('home:home')
    context = {
        'show_form': show_form,
    }
    #if admin
    return render(request, 'home/update.html', context)


def add_favorite(request, show):
    # try: 
        if request.method == 'POST':
            new_fav = Favorite.objects.create(
                show=Show.objects.get(shows_id=show)
            )
            # new_fav.is_favorite=True
            # # new_fav.is_favorite = not new_fav.is_favorite
            # new_fav.save()
            if new_fav.show.is_favorite:
                new_fav.show.is_favorite = False
                new_fav.save()
            else:
                new_fav.show.is_favorite = True
                new_fav.save()
            
            return redirect('home:favorites')
        else:
            # new_fav.save()
            return JsonResponse({'data': False})
    # except:
    #     return JsonResponse({'data': False})



def favorites(request):
    context = dict()
    
    context['new_fav'] = Favorite.objects.all()
    if request.GET:
        query = request.GET['q']
        new_fav = get_data_queryset(str(query))
    return render(request, "home/favorites.html", context=context)
                                                  # {'new_fav': new_fav}