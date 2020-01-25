from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import UserAccount
from django.contrib.auth.models import User


class OurForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['first_name', 'last_name','username','email', 'password']

	def save(self, commit=True):
		user = super(OurForm, self).save(commit=False)
		user.password = self.cleaned_data['password']
		if commit:
			user.save()

		return user