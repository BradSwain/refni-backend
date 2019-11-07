from rest_framework import serializers


# Configuration are created at submission time internally.
# User cannot create configurations separately via APIs.
class ConfigurationSerializer(serializers.Serializer):
    # created = serializers.DateTimeField(read_only=True)
    content = serializers.CharField(max_length=256, allow_blank=True)
    # submission = serializers.StringRelatedField(many=False, read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
