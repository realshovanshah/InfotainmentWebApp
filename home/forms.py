from django import forms
from .models import Show

class UploadShows(forms.ModelForm):
    class Meta:
        model = Show
        fields = ('shows_Name', 'shows_Description', 'shows_Type', 'shows_Genre', 'shows_Image')

