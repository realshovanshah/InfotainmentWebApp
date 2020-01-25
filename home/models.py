from django.db import models
from main.models import User
from model_utils import Choices

# Create your models here

class Show(models.Model):
	shows_id = models.AutoField(primary_key = True)
	shows_Name = models.CharField(max_length = 50)
	shows_Description = models.TextField()
	type_choices = Choices('TV Show','Movie')
	shows_Type = models.CharField(choices=type_choices, max_length=20)
	genre_choices = Choices('Sci-Fi','Drama', 'Romance', 'Comedy', 'Fantasy', 'Thriller')
	shows_Genre = models.CharField(choices=genre_choices, max_length=20) #choices = (('Movie'), ('Series'))
	shows_Image = models.FileField(upload_to="shows/")
	users= models.ManyToManyField(User) #on delete error
	#feedback= models.ForeignKey(Feedback, on_delete=models.CASCADE)

	def __str__(self):
		return self.shows_name



class Genre(models.Model):
	genre_id = models.AutoField(primary_key=True)
	genre_name = models.CharField(max_length=40) 
	shows= models.ForeignKey(Show, on_delete=models.CASCADE)

	def __str__(self):
		return self.genre_name