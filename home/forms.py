from django import forms
from .models import Show, Recommendation

#fields for form in upload
class UploadShows(forms.ModelForm):
    class Meta:
        model = Show
        fields = ('shows_Name', 'shows_Description', 'shows_Type', 'shows_Genre', 'shows_Image')

#fields for form in recommendation
class RecommendationForm(forms.ModelForm):
	class Meta:
		model = Recommendation
		fields = ('Name', 'Email')