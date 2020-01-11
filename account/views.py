from django.shortcuts import render, redirect
from main.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import OurForm


# Create your views here.
def home(request):
	return render(request=request,template_name="pages/home.html")

def register(request):
	# return HttpResponse("I am <strong> awesome </strong>")
	if request.method == "POST":
		form = OurForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect('main:home')

	form = OurForm()
	return render(request=request, template_name="pages/register.html", 
 	 			context={"form": form}) 

def user_logout(request):
	logout(request)
	return redirect('main:home')

def user_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				messages.success(request, f'you have logged as {{ username }}') #.info,.error
				return redirect('main:home')

	form = AuthenticationForm()
	return render(request, "pages/login.html", 
		context={"form":form})