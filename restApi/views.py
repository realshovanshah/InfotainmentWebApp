from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from home.models import Show
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def api_data(request):
     if request.method == "GET":
        show = Show.objects.all() 
        dict_type = {"shows": list(show.values("shows_Name", "shows_Description"))}
        return JsonResponse(dict_type)
@csrf_exempt   
def edited_data(request, pk):
    show = Show.objects.get(pk = pk)
    if request.method == "GET":
        return JsonResponse({"shows_name": show.shows_Name, "description": show.shows_Description})

    else:
        json_data = request.body.decode('utf-8')
        update_data = json.loads(json_data)
        show.shows_Name = update_data['shows_name']
        show.shows_Description = update_data['description']
        show.save()
        return JsonResponse({'message': 'Upadated Successfully!!'})