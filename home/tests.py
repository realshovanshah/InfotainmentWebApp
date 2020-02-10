from django.test import TestCase
from home.models import Show
# from datetime import datetime

# Create your tests here.

class HeraldTest(TestCase):
	def setUp(self):
		Show.objects.create(shows_Name="hey", shows_Description="hahaha")
		Show.objects.create(shows_Name="watch", shows_Description="Please wait to watch")

	def test_ORM(self):
		e1 = Show.objects.get(shows_Name="hey")
		e2 = Show.objects.get(shows_Name="watch")
		self.assertEqual(e1.shows_Name, "hey")
		self.assertEqual(e2.shows_Name, "watch")