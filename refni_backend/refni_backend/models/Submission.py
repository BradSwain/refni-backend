from django.db import models
from django.contrib.auth.models import User


# A model for user submission.
class Submission(models.Model):
    STATUS_CHOICES = (
        ('UPL', 'File uploaded'),
        ('RDY', 'Ready for evaluation'),
        ('ICP', 'Information incomplete'),
        ('CCL', 'Cancelled'),
        ('TIQ', 'Task waiting in queue'),
        ('WIP', 'Evaluation in progress'),
        ('FIN', 'Evaluation finished'),
        ('ERR', 'Error occurred'),
        ('UNA', 'Unavailable'),
    )
    TYPE_CHOICES = (
        ('RL', 'Repository Link Upload'),
        ('FU', 'File Upload'),
    )
    created = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    # We'll use the default django user model
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    # We allow uploading via github link or file upload
    repo = models.URLField(max_length=200)
    # Should we enforce the File to be a zipped/gzipped archive?
    # Should we allow them to upload folders directly? (I guess not)
    attachment = models.FileField()

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['created']
