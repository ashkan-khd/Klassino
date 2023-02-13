from django.utils import timezone
from rest_framework import serializers

from teaching.models import CourseSession, Course, Subject
from user.serializers import TeacherSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'grade']


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Course
        fields = ['teacher', 'subject']


class CourseSessionSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    login_url = serializers.SerializerMethodField()

    class Meta:
        model = CourseSession
        fields = ['start_time', 'end_time', 'course', 'login_url']

    def get_login_url(self, obj):
        if obj.start_time - timezone.timedelta(minutes=5) <= timezone.now() <= obj.end_time + timezone.timedelta(minutes=5):
            return obj.generate_login_url(self.context['request'].user.student)
        else:
            return None
