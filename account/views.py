from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import OurForm


# Create your views here.
def home(request):
	return render(request=request,template_name="home/home.html")


def register(request):
    if request.method == 'POST':
        form = OurForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('main:home')
        else:            
            return render(request, "account/register.html",{'form':form})
    else:
        form = OurForm()
        return render(request, "account/register.html", {"form":form})


def user_logout(request):
	logout(request)
	return redirect('main:register')

def user_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request,username=username, password=password)
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			if user is not None:
				login(request, user)
				return redirect('main:home')
		else:
			messages.info(request, f'Invalid username or password')
			return render(request, "account/login.html",context={"form": form})
	else:
		form = AuthenticationForm()
		return render(request, "account/login.html",context={"form": form})

