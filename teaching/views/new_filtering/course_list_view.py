from django.utils import timezone
from rest_framework import generics

from teaching.models import Course
from teaching.views.new_filtering.serializers import CourseCardSerializer
from teaching.views.new_filtering.paginators import CoursesPagePaginator


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCardSerializer
    pagination_class = CoursesPagePaginator

    def get_queryset(self):
        qs = super().get_queryset().filter(start_time__gte=timezone.now())
        return qs.filter(subject=self.request.query_params.get('subject'))

