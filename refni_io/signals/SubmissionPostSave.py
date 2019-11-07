from refni_io.tasks import dispatch_submission
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender='refni_io.Submission', dispatch_uid="dispatch_submission")
def dispatch_task(sender, **kwargs):
    sub = kwargs['instance']
    dispatch_submission.delay(sub.id)
