from refni_backend.celery import *
from refni_io.models.Submission import Submission


@app.task
def dispatch_submission(sid):
    print(sid, 'DISPATCHING TO ANALYZER')
    # Here do the real dispatching
    submission = Submission.objects.get(id=sid)
    submission.mark_ready()
