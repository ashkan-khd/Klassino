from rest_framework import serializers

from mentoring.models import AssistancePackage


class AssistancePackageSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError

    class Meta:
        model = AssistancePackage
        fields = ['id', 'duration_days', 'price', 'description']
