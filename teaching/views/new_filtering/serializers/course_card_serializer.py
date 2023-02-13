from rest_framework import serializers

from teaching.models import Course
from teaching.views.course_page.serializers import SubjectSerializer
from user.serializers import TeacherSerializer


class CourseCardSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    teacher = TeacherSerializer()
    subscription_count = serializers.IntegerField(source='subscriptions.count')

    class Meta:
        model = Course
        fields = ['id', 'teacher', 'subject', 'price', 'start_time', 'end_time', 'subscription_count']