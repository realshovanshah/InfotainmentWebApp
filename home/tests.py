from django.test import TestCase
from home.models import Show
# from datetime import datetime

# Create your tests here.

class HeraldTest(TestCase):
def setUp(self):
Show.objects.create(shows_name="hey", shows_description="hahaha", )
Show.objects.create(shows_name="watch", shows_description="Pleasw wait to watch", )
# date=datetime.now()

def test_ORM(self):
e1 = Show.objects.get(shows_name="hey")
e2 = Show.objects.get(shows_name="watch")
self.assertEqual(e1.shows_name, "hey")
self.assertEqual(e2.shows_name, "Please wait to watch")