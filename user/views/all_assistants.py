from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from user.models import Assistant
from user.serializers import AssistantSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10


class AssistantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Assistant.active_objects.filter(packages__isnull=False).distinct('id').all().order_by('id')
    serializer_class = AssistantSerializer
    pagination_class = CustomPagination
