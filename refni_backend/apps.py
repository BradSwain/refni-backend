from django.apps import AppConfig


class RefniBackendConfig(AppConfig):
    name = 'refni_backend'

    def ready(self):
        from django.db.models.signals import post_save
        from refni_io.signals.SubmissionPostSave import dispatch_task

        post_save.connect(dispatch_task, sender='refni_io.Submission',
                          dispatch_uid='submission_dispatch')
