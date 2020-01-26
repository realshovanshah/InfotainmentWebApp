from django.test import TestCase
from Comment.models import Comment

# Create your tests here.

class CommentTest(TestCase):
def setUp(self):
Comment.objects.create(comment_name="feedback", comment_description="give feedback", )
Comment.objects.create(comment_name="error", comment_description="error giving feedback", )


def test_ORM(self):
t1 = Comment.objects.get(comment_name="feedback")
t2 = Comment.objects.get(comment_name="error")
self.assertEqual(t1.comment_name, "give feedback")
self.assertEqual(t2.comment_name, "error giving feedback")