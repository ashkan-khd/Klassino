from rest_framework import viewsets

from user.models import Teacher, Assistant
from user.serializers import TopTeacherSerializer, TopAssistantSerializer


class TopTeacherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Teacher.active_objects.filter(is_top=True)
    serializer_class = TopTeacherSerializer


class TopAssistantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Assistant.active_objects.filter(is_top=True)
    serializer_class = TopAssistantSerializer
