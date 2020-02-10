from django.db import models
from main.models import User   
from home.models import Show
 
class Feedback(models.Model):
    feedback_owner = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    feedback_show = models.ForeignKey(Show, on_delete=models.CASCADE, default=0, null=True)
    feedback = models.CharField(max_length = 255)
   
    def __str__(self):
        return str(self.feedback)