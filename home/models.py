from django.db import models
from main.models import User

#class for all movies and series in our application and their description.
class Show(models.Model):
	shows_id = models.AutoField(primary_key = True)
	shows_name = models.CharField(max_length = 50)
	shows_description = models.TextField()
	shows_type = models.CharField(max_length = 20)
	users= models.ManyToManyField(User)
	
	def __str__(self):
		return self.shows_name


#genre for all the movies and series
class Genre(models.Model):
	genre_id = models.AutoField(primary_key=True)
	genre_name = models.CharField(max_length=40) 
	shows= models.ForeignKey(Show, on_delete=models.CASCADE)

	def __str__(self):
		return self.genre_name