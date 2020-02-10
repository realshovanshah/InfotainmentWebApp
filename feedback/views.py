from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import FeedbackForm
from account.forms import OurForm
from home.models import Show
from .models import Feedback
from django.contrib.auth.models import User

#shows feedback
def show_feedback(request):
    feedback = Feedback.objects.all()
    return render(request, "feedback/details.html", context={'feedback':feedback})


#to give comments and reviews about shows
def feedback(request, pk):
    show=Show.objects.get(pk=pk)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        show=Show.objects.get(pk=pk)
        print(show)
        print(request.user.id)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.feedback_owner_id = request.user.id
            feedback.feedback_show_id = show.shows_id
            feedback.save()
            print(request.user.id)

        return redirect('main:home')
    
    form = FeedbackForm()
    return render(request, 'feedback/feedback.html', {'form':form, 'show':show})


#deletes the given feedback
def delete_feedback(request, pk):
    feedback = Feedback.objects.get(pk=pk)
    feedback.delete()
    return redirect('/details')