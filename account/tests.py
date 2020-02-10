from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

class AccountTest(TestCase):
	def setUp(self):
		User.objects.create_user(username="account", password="user")
		User.objects.create_user(username="shovan", password="shah")

	def test_ORM(self):
		a1 = User.objects.get(username="account")
		self.assertEqual(a1.username, "account")


