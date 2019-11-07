from refni_io.serializers.Submission import SubmissionSerializer
from refni_io.models.Submission import Submission
from rest_framework import viewsets
from rest_framework import permissions


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    # permission_classes = (permissions.DjangoModelPermissions, )
