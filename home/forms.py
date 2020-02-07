from django import forms
from .models import Show, Recommendation

class UploadShows(forms.ModelForm):
    class Meta:
        model = Show
        fields = ('shows_Name', 'shows_Description', 'shows_Type', 'shows_Genre', 'shows_Image')

class RecommendationForm(forms.ModelForm):
	class Meta:
		model = Recommendation
		fields = ('Name', 'Email')