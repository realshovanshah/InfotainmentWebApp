from django.db import models
from main.models import User

# class UserAccount(models.Model):
#     first_name = models.CharField(max_length=200,null=True)
#     last_name = models.CharField(max_length=200)
#     username = models.CharField(max_length=200)
#     email = models.EmailField()
#     password = models.CharField(max_length=200)

# Create your models here.
#GENRE, USER, MOVIES&TV, REVIEWS
# class User(models.Model):
# 	user_id = models.AutoField(primary_key = True)
# 	user_name = models.CharField(max_length=40)
# 	user_email = models.EmailField()
# 	user_password = models.CharField(max_length=20)
# 	user_description = models.TextField()

#feedback app ma halne yeslai paxi
# class Feedback(models.Model):
# 	feedback_id = models.AutoField(primary_key=True)
# 	feedback_date = models.DateTimeField(auto_now_add=True)
# 	feedback_body = models.TextField()
# 	users = models.ForeignKey(User, on_delete=models.CASCADE)

	# TODO shows=models



	#watchlist,fav......feedback/property....

# class Show(models.Model):
# 	shows_id = models.AutoField(primary_key = True)
# 	shows_name = models.CharField(max_length = 50)
# 	shows_description = models.TextField()
# 	shows_type = models.CharField(max_length = 20) #choices = (('Movie'), ('Series'))
# 	users= models.ManyToManyField(User) #on delete error
# 	feedback= models.ForeignKey(Feedback, on_delete=models.CASCADE)
# # Create your models here.

# 	def __str__(self):
# 		return self.shows_name


# class Genre(models.Model):
# 	genre_id = models.AutoField(primary_key=True)
# 	genre_name = models.CharField(max_length=40) 
# 	shows= models.ForeignKey(Show, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.genre_name