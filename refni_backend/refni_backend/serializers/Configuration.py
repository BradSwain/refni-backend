from rest_framework import serializers


# Configuration are created at submission time internally.
# User cannot create configurations separately via APIs.
class ConfigurationSerializer(serializers.Serializer):
    created = serializers.DateTimeField(read_only=True)
    content = serializers.CharField(read_only=True)
    submission = serializers.StringRelatedField(many=False, read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
