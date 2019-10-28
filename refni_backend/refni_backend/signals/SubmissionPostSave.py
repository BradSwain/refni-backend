from refni_backend.refni_backend.tasks import dispatch_submission


def dispatch_task(sender, **kwargs):
    dispatch_submission()
