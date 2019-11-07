from rest_framework import serializers


# All fields read only.
class EvalReportSerializer(serializers.Serializer):
    created = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(read_only=True)
    content = serializers.CharField(read_only=True)
    submission = serializers.StringRelatedField(many=False, read_only=True)
    eval_start_time = serializers.DateTimeField(read_only=True)
    eval_end_time = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
