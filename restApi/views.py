from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from home.models import Show
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#Getting datas stored in the app
def api_data(request):
     if request.method == "GET":
        show = Show.objects.all() 
        dict_type = {"shows": list(show.values("shows_id","shows_Name", "shows_Description"))}
        return JsonResponse(dict_type)

#Getting a specific data with primary key
def api_get_data(request, pk):
    if request.method == "GET":
        try:
            show = Show.objects.get(pk = pk)
            response = json.dumps([{'shows_id':show.shows_id,'shows_Name':show.shows_Name, 'shows_Description':show.shows_Description}])
            return HttpResponse(response, content_type='text/json')
        except:
            return JsonResponse({"Not Found":"Nothing found of that ID"})

#Updating and deleting existing data using primary key
@csrf_exempt
def api_update_data(request, pk):
    show = Show.objects.get(pk=pk)
    if request.method == "PUT":
        json_data = request.body.decode('utf-8')
        updating = json.loads(json_data)
        show.shows_id=updating['shows_id']
        show.shows_Name = updating['shows_Name']
        show.shows_Description = updating['shows_Description']
        show.save()
        return JsonResponse({"Updated":"Successfully Updated!!"})
    elif request.method == "DELETE":
        show.delete()
        return JsonResponse({"Deleted":"Successfully Deleted!!"})

#Adding new data into the app
@csrf_exempt
def api_add_data(request):
    if request.method == "POST":
        json_data = request.body.decode('utf-8')
        adding = json.loads(json_data)
        shows_id = adding['shows_id']
        shows_Name = adding['shows_Name']
        shows_Description = adding['shows_Description']
        
        show = Show.objects.create(shows_id= shows_id,shows_Name = shows_Name, shows_Description = shows_Description)
        try:
            show.save()

            return JsonResponse({"Created":"Show has been added"})

        except:

            return JsonResponse({"Error":"Show is unable to be added"})


#Pagination of the api when there is too much data.
def api_pagination(request, PAGENO, SIZE):
    if request.method == "GET":
        skip = SIZE * (PAGENO -1)
        show = Show.objects.all() [skip:(PAGENO * SIZE)]
        dictionary_type = {"show":list(show.values("shows_Name", "shows_Description", "shows_Genre", "shows_Image", "shows_Name", "shows_Type", "shows_id"))}
    return JsonResponse(dictionary_type)