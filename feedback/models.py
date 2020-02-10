from django.db import models
# from django.contrib.auth.models import User
from main.models import User   
from home.models import Show
 
# Create your models here.
class Feedback(models.Model):
    # image = models.ForeignKey(Post,blank=True, on_delete=models.CASCADE )
    feedback_owner = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    feedback_show = models.ForeignKey(Show, on_delete=models.CASCADE, default=0, null=True)
    feedback = models.CharField(max_length = 255)
   
    def __str__(self):
        return str(self.feedback)