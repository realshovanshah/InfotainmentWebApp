from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import FeedbackForm
from account.forms import OurForm
from home.models import Show
from .models import Feedback
from django.contrib.auth.models import User


# Create your views here.

def details(request):
    return render(request=request,template_name="feedback/details.html")


def show_feedback(request, pk):
    # detail = User.objects.get(pk = pk)
    feedback = Feedback.objects.all()
    # if request.user.is_authenticated:
    return render(request, "feedback.html", context={'feedback':feedback})
    # else:
        # return redirect('main:home')


def feedback(request,shows_id):
    # user=User.objects.get(pk=pk)
    # current_user=request.user
    # profile_owner = User.objects.get(username=current_user)
    # feedback = Feedback.objects.create(
    #     feedback_owner = User.objects.get(pk=request.user.id), 
    #     feedback_show = Show.objects.get(shows_id=show)
    #     )  
    feedback = Feedback.objects.get(pk=request.user.id, feedback_owner=shows_id)
    print(feedback)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.feedback_owner_id = request.user.id
            feedback.feedback_show_id = shows_id
            feedback.save()
            print(request.user.id)
            print(shows_id)

        return redirect('main:home')

    
    form = FeedbackForm()
    return render(request, 'feedback/feedback.html', {'form':form})