import datetime

from django.utils import timezone, dateparse
from django.utils.timezone import make_aware, is_aware
from jalali_date import datetime2jalali
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from mentoring.models import AssignedStudyPeriod
from mentoring.serializers import AssignedStudyPeriodSerializer, NewAssignedStudyPeriodSerializer
from user.permissions import IsStudent, IsAssistant, IsAssistantToStudent


class GetWeekMixin:
    def get_week(self):
        current_time = timezone.now()
        time = self.request.query_params.get('time', current_time)
        if isinstance(time, str):
            time = dateparse.parse_datetime(time) or current_time

        jalali = datetime2jalali(time)
        return time - timezone.timedelta(
            days=jalali.weekday(),
            hours=jalali.hour,
            minutes=jalali.minute,
            microseconds=jalali.microsecond
        )


class AssignedStudyPeriodStudentView(viewsets.ModelViewSet, GetWeekMixin):
    serializer_class = AssignedStudyPeriodSerializer
    authentication_classes = [TokenAuthentication]

    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [IsAuthenticated, IsStudent]

    def get_queryset(self):
        return self.request.user.student.assigned_study_periods.filter(
            start_time__gte=self.get_week(),
            start_time__lt=self.get_week() + timezone.timedelta(days=7)
        ).all()


class AssignedStudyPeriodAssistantView(viewsets.ModelViewSet, GetWeekMixin):
    authentication_classes = [TokenAuthentication]

    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [
        IsAuthenticated,
        IsAssistant,
        IsAssistantToStudent,
    ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AssignedStudyPeriodSerializer
        else:
            return NewAssignedStudyPeriodSerializer

    def get_queryset(self):
        if self.request.method == 'DELETE':
            return self.request.user.assistant.assigned_by_study_periods.filter(is_deleted=False)
        return self.request.user.assistant.assigned_by_study_periods.filter(
            student_id=self.request.query_params.get('student_id'),
            start_time__gte=self.get_week(),
            start_time__lt=self.get_week() + timezone.timedelta(days=7),
            is_deleted=False,
        ).all()

    def perform_create(self, serializer):
        serializer.save(assistant=self.request.user.assistant)
