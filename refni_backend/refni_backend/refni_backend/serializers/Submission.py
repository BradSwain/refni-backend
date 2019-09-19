from rest_framework import serializers
from refni_backend.refni_backend.refni_backend.models.Submission import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
