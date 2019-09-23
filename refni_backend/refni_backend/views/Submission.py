from refni_backend.refni_backend.serializers.Submission import SubmissionSerializer
from refni_backend.refni_backend.models.Submission import Submission
from rest_framework import viewsets
from rest_framework import permissions


class SubmissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.DjangoModelPermissions)
