from django.db import models
from django.db.models import F, ExpressionWrapper
from django.db.models.functions import Cast
from django.utils import timezone
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from mentoring.models import AssistanceCourse
from mentoring.services import find_active_assistance_courses
from user.models import Student
from user.permissions import IsAssistant
from user.serializers import generate_details_serializer


class MentoredStudentsViewSet(mixins.ListModelMixin,
                              viewsets.GenericViewSet):
    serializer_class = generate_details_serializer(Student)
    permission_classes = [IsAuthenticated, IsAssistant]

    def get_queryset(self):
        return Student.objects.filter(
            id__in=find_active_assistance_courses().filter(
                assistance_package__assistant=self.request.user.assistant,
            ).values_list('student_id', flat=True)
        )
