from rest_framework import serializers
from refni_backend.refni_backend.models.Submission import Submission
from refni_backend.refni_backend.serializers.User import UserSerializer
from refni_backend.refni_backend.models.Configuration import Configuration
from refni_backend.refni_backend.serializers.Configuration import ConfigurationSerializer
from django.contrib.auth.models import User
from django.db import transaction
from datetime import datetime


class SubmissionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    tag = serializers.CharField(max_length=100, allow_blank=True, default='')
    status = serializers.ChoiceField(choices=Submission.STATUS_CHOICES, read_only=True)
    description = serializers.CharField(allow_blank=True, default='')
    report = serializers.CharField(allow_blank=True, default='', read_only=True)
    type = serializers.ChoiceField(choices=Submission.TYPE_CHOICES, allow_null=False)
    repo = serializers.URLField(allow_null=True, allow_blank=True)
    attachment = serializers.FileField(allow_null=True, allow_empty_file=False, use_url=False)

    user = UserSerializer(allow_null=False)
    configuration = ConfigurationSerializer(allow_null=True, default=None)

    @transaction.atomic
    def create(self, validated_data):
        email = validated_data.pop('user')['email']
        user, _ = User.objects.get_or_create(email=email, defaults={
            'username': email, 'email': email, 'password': User.objects.make_random_password()})

        config = validated_data.pop('configuration')
        sub = Submission.objects.create(user=user, status=Submission.STATUS_CHOICES[0][0], **validated_data)
        Configuration.objects.create(submission=sub, **config)
        return sub

    # Probably we shouldn't allow updates (at least from outside).
    # Upload again if you would like to change the configuration.
    def update(self, instance, validated_data):
        pass

    def validate(self, attrs):
        if attrs['attachment'] is None and attrs['type'] == Submission.TYPE_CHOICES[1][0]:
            raise serializers.ValidationError('Please upload file if you choose your upload type to be "File Upload".')
        if (attrs['repo'] is None or attrs['repo'] == '') and attrs['type'] == Submission.TYPE_CHOICES[0][0]:
            raise serializers.ValidationError('Please enter repository URL if you choose your upload '
                                              'type to be "Repository Link Upload".')
        if attrs['user']['email'] is None or attrs['user']['email'].strip() == '':
            raise serializers.ValidationError('Email cannot be empty.')
        return attrs

