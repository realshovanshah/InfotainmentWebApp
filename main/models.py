from django.db import models


class User(models.Model):
	user_id = models.AutoField(primary_key = True)
	user_name = models.CharField(max_length=40)
	user_email = models.EmailField()
	user_password = models.CharField(max_length=20)
	user_description = models.TextField()
