from refni_backend.refni_backend.serializers.EvalReport import EvalReportSerializer
from refni_backend.refni_backend.models.EvalReport import EvalReport
from rest_framework import viewsets
from rest_framework import permissions


class EvalReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EvalReport.objects.all()
    serializer_class = EvalReportSerializer
    # permission_classes = (permissions.DjangoModelPermissions, )
