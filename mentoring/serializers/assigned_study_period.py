from rest_framework import serializers, renderers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import empty

from mentoring.models import AssignedStudyPeriod
from mentoring.services import has_conflict
from user.models import Student


class AssignedStudyPeriodSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        raise NotImplementedError

    class Meta:
        model = AssignedStudyPeriod
        fields = ['id', 'title', 'start_time', 'end_time', 'description']


class NewAssignedStudyPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedStudyPeriod
        fields = ['title', 'start_time', 'end_time', 'description', 'student']

    def create(self, validated_data):
        if validated_data['start_time'] >= validated_data['end_time']:
            raise ValidationError('زمان شروع باید قبل از زمان پایان باشد')
        if has_conflict(
                validated_data['student'],
                validated_data['start_time'],
                validated_data['end_time']
        ):
            raise ValidationError('زمان مطالعه ثبت شده با بقیه زمان‌های مطالعه برخورد دارد!')

        return super().create(validated_data)
