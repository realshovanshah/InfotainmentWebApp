from django.test import TestCase
from home.models import Show
# from datetime import datetime

# Create your tests here.

class HeraldTest(TestCase):
	def setUp(self):
		Show.objects.create(shows_name="hey", shows_description="hahaha", )
		# date=datetime.now()

	def test_ORM(self):
		t = Show.objects.get(shows_name="hey")
		self.assertEqual(t.shows_name, "hey")