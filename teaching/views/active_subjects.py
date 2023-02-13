from django.db.models import Exists, OuterRef
from django.utils import timezone
from rest_framework import viewsets, mixins

from teaching.models import Subject, Course
from teaching.serializers import SubjectSerializer


class ActiveSubjectsView(mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.annotate(has_active_course=Exists(
        Course.objects.filter(
            start_time__gte=timezone.now(),
            subject=OuterRef('pk')
        )
    )).filter(has_active_course=True)
