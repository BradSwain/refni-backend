from rest_framework import serializers
from refni_backend.refni_backend.models.Submission import Submission
from refni_backend.refni_backend.models.Configuration import Configuration


class SubmissionSerializer(serializers.Serializer):
    created = serializers.DateTimeField(read_only=True)
    tag = serializers.CharField(max_length=100, allow_blank=True, default='')
    status = serializers.ChoiceField(choices=Submission.STATUS_CHOICES, read_only=True)
    description = serializers.CharField(allow_blank=True, default='')
    report = serializers.CharField(allow_blank=True, default='')
    type = serializers.ChoiceField(choices=Submission.TYPE_CHOICES, read_only=True)
    user = serializers.SerializerMethodField('_get_user')

    def _get_user(self, _obj):
        request = getattr(self.context, 'request', None)
        if request:
            return request.user

    def create(self, validated_data):
        sub = Submission.objects.create(**validated_data)
        Configuration.objects.create({'content': validated_data['config'], 'submission': sub})
        return sub

    # Probably we shouldn't allow updates (at least from outside).
    # Upload again if you would like to change the configuration.
    def update(self, instance, validated_data):
        pass

