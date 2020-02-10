from django.db import models
from django.contrib.auth.models import User
from home.models import Show
 
# Create your models here.
class Feedback(models.Model):
    # image = models.ForeignKey(Post,blank=True, on_delete=models.CASCADE )
    feedback_owner = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    feedback_show = models.ForeignKey(Show, on_delete=models.CASCADE, default=0)
    feedback = models.TextField()

    # def save_comment(self):
    #     self.save()

    # def delete_comment(self):
    #     self.delete()
   
    def __str__(self):
        return str(self.feedback)