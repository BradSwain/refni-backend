from django.db import models
from refni_backend.refni_backend.models.Submission import Submission


# A model for evaluation report
class EvalReport(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=False, default='Report')
    content = models.TextField()
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE)

    # Evaluation
    eval_start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    eval_end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
