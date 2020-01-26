from django.test import TestCase

# Create your tests here.

class AccountTest(TestCase):
def setUp(self):
Account.objects.create(account_name="account", account_body="user", )
Account.objects.create(account_name="login", account_body="can't login", )


def test_ORM(self):
a1 = Account.objects.get(account_name="account")
a2 = Account.objects.get(account_name="login")
self.assertEqual(a1.account_name, "account")
self.assertEqual(a2.account_name, "can't login")