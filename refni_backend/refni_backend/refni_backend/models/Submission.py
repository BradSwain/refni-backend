from django.db import models


class Submission(models.Model):
    STATUS_CHOICES = (
        ('RDY', 'Ready for evaluation'),
        ('WIP', 'Evaluation in progress'),
        ('FIN', 'Evaluation finished'),
        ('ERR', 'Evaluation error'),
        ('UNA', 'Unavailable'),
    )
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    description = models.TextField()
    report = models.TextField()
    # We allow uploading via github link or file upload
    git_repo = models.URLField(max_length=200)
    attachments = models.FileField()

    class Meta:
        ordering = ['created']
