from refni_backend.refni_backend.tasks import dispatch_submission


def dispatch_task(sender, **kwargs):
    sub = kwargs['instance']
    if kwargs['create']:
        dispatch_submission.delay(sub)
