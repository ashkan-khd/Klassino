import django_filters
from django_filters import FilterSet
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from announcement.models import Announcement
from announcement.serializers import AnnouncementSerializer


class AnnouncementPaginator(PageNumberPagination):
    page_size = 5


class PagesFilterSet(FilterSet):
    class Meta:
        model = Announcement
        fields = {
            'main_page': ['exact'],
            'student_page': ['exact']
        }


class AnnouncementViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = AnnouncementPaginator
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = PagesFilterSet
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        return super().get_queryset().order_by('-created')
