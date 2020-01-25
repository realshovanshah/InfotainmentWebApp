from django import forms
from .models import Show

class UploadShows(forms.ModelForm):
    class Meta:
        model = Show
        fields = ('shows_name', 'shows_description', 'shows_type', 'shows_genre', 'shows_image')

