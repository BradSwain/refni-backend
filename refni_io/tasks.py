from refni_backend.celery import *


@app.task
def dispatch_submission(submission):
    print(submission.id, 'DISPATCHING TO ANALYZER')
    # Here do the real dispathcing
    submission.mark_ready()
