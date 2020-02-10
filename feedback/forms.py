from django import forms

from .models import Feedback

#for form in feedback
class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields =['feedback']