from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

class UserTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='nepal', email='nepal@gmail.com', password='nepal')
        User.objects.create_user(username='great', email='great@gmail.com', password='nep')

    def test_user(self):
        u1 = User.objects.get(username = 'nepal')
        u2 = User.objects.get(username= 'great')
        self.assertEqual(u1.username, 'nepal')
        self.assertEqual(u2.username, 'great')
