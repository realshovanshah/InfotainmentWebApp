from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import CommentForm
from account.forms import OurForm
from home.models import Show
from .models import Comment
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request=request,template_name="home/home.html")

def comment(request):
    current_user=request.user
    # image = Show.objects.get(id=image_id)
    profile_owner = User.objects.get(username=current_user)
    comments = Comment.objects.all()
    print(comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # comment.image = image
            comment.comment_owner = current_user
            comment.save()

            print(comments)


        return redirect('main:home')

    
    form = CommentForm()
    return render(request, 'pages/feedback.html', {'form':form})