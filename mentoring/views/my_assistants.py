from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from mentoring.serializers import AssistantContactSerializer
from mentoring.services import find_active_assistance_courses
from user.models import Assistant
from user.permissions import IsStudent


class MyAssistants(viewsets.ModelViewSet):
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [IsAuthenticated, IsStudent]
    serializer_class = AssistantContactSerializer

    def get_queryset(self):
        student = self.request.user.student
        return Assistant.active_objects.filter(
            id__in=find_active_assistance_courses().filter(
                student=student,
            ).values_list('assistance_package__assistant', flat=True)
        )
