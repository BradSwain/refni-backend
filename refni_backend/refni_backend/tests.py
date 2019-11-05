from django.test import TestCase
from refni_backend.refni_backend.models.Submission import Submission


# Create your tests here.
class SubmissionTestCase(TestCase):
    def setUp(self):
        Submission.objects.create(tag='tag')

    def test_submission_exists(self):
        s = Submission.objects.get(tag='tag')
        self.assertEqual(s.tag, 'tag')
