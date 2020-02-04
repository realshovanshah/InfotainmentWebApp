from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

class AccountTest(TestCase):
def setUp(self):
User.objects.create(username="account", password="user", )

def test_ORM(self):
a1 = User.objects.get(account_name="account")
self.assertEqual(a1.username, "account")
