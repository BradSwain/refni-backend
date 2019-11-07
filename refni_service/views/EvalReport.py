from refni_io.serializers.EvalReport import EvalReportSerializer
from refni_io.models.EvalReport import EvalReport
from rest_framework import viewsets
from rest_framework import permissions


class EvalReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EvalReport.objects.all()
    serializer_class = EvalReportSerializer
    # permission_classes = (permissions.DjangoModelPermissions, )
