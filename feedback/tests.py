from django.test import TestCase
from feedback.models import Feedback
from main.models import User
# from django.contrib.auth.models import User
from .models import Feedback
from home.models import Show

# Create your tests here.

class FeedbackTest(TestCase):

		def setUp(self):
		u = User.objects.create(user_name="lol", user_email="lol@gmail.com")
		# Feedback.objects.create(feedback_owner=user, feedback_show="give feedback" )
		s = Show.objects.create(shows_Name="coollol")
		e = Feedback.objects.create(feedback_owner= u, feedback_show=s, feedback = "lala" )
		# Feedback.objects.create(feedback_owner = "EricLapton", feedback_show=1, feedback="RATED")


	def test_ORM(self):
		user = User.objects.get(user_name="lol")
		feedback = Feedback.objects.get(feedback="lala")
		self.assertEqual(user.user_name,"lol")
		self.assertEqual(feedback.feedback, "lala")