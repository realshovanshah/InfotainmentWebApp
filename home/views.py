from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Show, Favorite, Recommendation
from .forms import UploadShows
from django.db.models import Q
from .forms import UploadShows, RecommendationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='account:login')
def recommendation(request):
        return render(request=request,template_name="home/recommendation.html")

#function for homepage and listing the shows.
@login_required(login_url='account:login')
def home(request):
    show = Show.objects.all()
    if request.GET:
        query = request.GET['q']
        show = get_data_queryset(str(query))
    return render(request, 'home/home.html', {'shows': show})

 
#function for uploading.
@login_required(login_url='account:login')
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

@login_required(login_url='account:login')
def delete_show(request, pk):
    show = Show.objects.get(pk=pk)
    show.delete()
    return redirect('home:home')

@login_required(login_url='account:login')
def delete_fav(request, pk=None):
    fav = Favorite.objects.get(pk=pk)
    # show = get_object_or_404(Show, pk=pk)
    fav.delete()
    fav.shows.is_favorite= False
    fav.shows.save()
    return redirect('home:favorites')

@login_required(login_url='account:login')
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

@login_required(login_url='account:login')
def add_favorite(request,pk=None):
    if request.method == 'POST':
        show = get_object_or_404(Show, pk=pk)
        show.is_favorite= True
        show.save()
        # f=Favorite(user_id=request.user.id)
        Favorite.objects.create(shows_id=show.shows_id)
        # f.shows_id=pk
        # f.fav_status=True
        # f.save()
        messages.success(request, 'Successfully Favorited!!!.')
        return redirect('home:home')
        # else:
        #     show.is_favorite = False
        #     show.save()
    return render(request, 'home/favorites.html')
        
@login_required(login_url='account:login')
def favorites(request):
    # new_fav= Favorite.objects.filter(user_id=request.user.id)
    new_fav= Favorite.objects.all()
    return render(request, 'home/favorites.html', {"new_fav":new_fav})