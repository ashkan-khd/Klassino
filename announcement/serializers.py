from rest_framework import serializers

from announcement.models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = [
            'title',
            'context',
            'created'
        ]
