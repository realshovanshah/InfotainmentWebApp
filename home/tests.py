from django.test import TestCase
from home.models import Show, Favorite, Recommendation

#test to check Shows
class ShowTest(TestCase):
	def setUp(self):
		Show.objects.create(shows_Name="office", shows_Description="comedy")
		Show.objects.create(shows_Name="friends", shows_Description="friends comedy")

	def test_ORM(self):
		e1 = Show.objects.get(shows_Name="office")
		e2 = Show.objects.get(shows_Name="friends")
		self.assertEqual(e1.shows_Name, "office")
		self.assertEqual(e2.shows_Name, "friends")


#Testing of Recommendation
class RecommendationTest(TestCase):
	def setUp(self):
		Recommendation.objects.create(Name = "win")
		Recommendation.objects.create(Email = "win@gmail.com")

	def test_ORM(self):
		r1 = Recommendation.objects.get(Name = "win")
		r2 = Recommendation.objects.get(Email = "win@gmail.com")
		self.assertEqual(r1.Name,"win")
		self.assertEqual(r2.Email,"win@gmail.com")

