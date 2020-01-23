from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Comment(models.Model):
    # image = models.ForeignKey(Post,blank=True, on_delete=models.CASCADE )
    comment_owner = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    comment = models.TextField()

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

   
    def __str__(self):
        return str(self.comment)