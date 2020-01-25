from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import OurForm


#this function is for homepage.
def home(request):
	return render(request=request,template_name="home/home.html")



#this function is for creating form and determining whether the form is valid or not.
def register(request):
    if request.method == 'POST':
        form = OurForm(data=request.POST)
        if form.is_valid():  #redirects to homepage only if the form is valid.
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


#this function logs user out when logged in
def user_logout(request):
	logout(request)
	return redirect('main:register')


#this function is for user to login if they have an account.
def user_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request,username=username, password=password)
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():  #logins user only if the details provided are valid.
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

