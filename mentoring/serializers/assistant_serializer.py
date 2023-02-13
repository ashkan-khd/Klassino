from rest_framework import serializers

from user.models import Assistant


class AssistantContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = [
            'id',
            'profile_image',
            'first_name',
            'last_name',
            'phone_number'
        ]
