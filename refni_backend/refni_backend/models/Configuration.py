from django.db import models
from refni_backend.refni_backend.models.Submission import Submission


# A model for evaluation configuration/settings
class Configuration(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    # This includes command line options, etc.
    # We can put everything in json into content, or we can create more fields
    content = models.TextField()
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
