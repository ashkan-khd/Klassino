from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from teaching.models import Course
from teaching.views.course_page.serializers import CourseSerializer, CourseSessionSerializer


class CoursePageView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseSessionView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CourseSessionSerializer

    def get_queryset(self):
        if 'course_pk' in self.request.query_params:
            course = get_object_or_404(Course, pk=self.request.query_params['course_pk'])
            return course.sessions.order_by('start_time')[:2]
        else:
            raise ValidationError('آیدی دوره لازم است.')
