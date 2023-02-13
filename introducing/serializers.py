from rest_framework.serializers import ModelSerializer

from introducing.models import TeacherIntroductionVideo, AssistantIntroductionVideo


class TeacherIntroductionVideoSerializer(ModelSerializer):
    class Meta:
        model = TeacherIntroductionVideo
        fields = ['aparat_id', 'embed_hash']


class AssistantIntroductionVideoSerializer(ModelSerializer):
    class Meta:
        model = AssistantIntroductionVideo
        fields = ['aparat_id', 'embed_hash']
