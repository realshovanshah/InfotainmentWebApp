from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import CommentForm
from account.forms import OurForm
from home.models import Show
from .models import Comment
from django.contrib.auth.models import User


# Create your views here.

def details(request):
    return render(request=request,template_name="feedback/details.html")

def comment(request):
    current_user=request.user
    # profile_owner = User.objects.get(username=current_user)
    comments = Comment.objects.all()
    print(comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_owner = current_user
            comment.save()

            print(comments)


        return redirect('main:home')

    
    form = CommentForm()
    return render(request, 'feedback/feedback.html', {'form':form})