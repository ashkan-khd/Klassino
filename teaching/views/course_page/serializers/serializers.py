from jalali_date import date2jalali
from rest_framework import serializers

from introducing.models import TeacherIntroductionVideo
from teaching.models import Course, Subject, CourseSession
from user.serializers import TeacherSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['grade', 'name']


class CourseSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    teacher = TeacherSerializer()
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    def get_start_time(self, obj):
        return date2jalali(obj.start_time).strftime('%Y/%m/%d')

    def get_end_time(self, obj):
        return date2jalali(obj.end_time).strftime('%Y/%m/%d')

    class Meta:
        model = Course
        fields = ['id', 'teacher', 'subject', 'price', 'start_time', 'end_time']


class CourseSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSession
        fields = ['start_time', 'end_time']