from django.utils import timezone
from rest_framework import viewsets
from rest_framework.settings import api_settings

from teaching.models import CourseSession
from teaching.serializers.my_desk_classes import CourseSessionSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsStudent


class MyDeskClassesViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSessionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [IsAuthenticated, IsStudent]

    def get_queryset(self):
        return CourseSession.objects.filter(
            course__subscriptions__student=self.request.user.student,
            end_time__gte=timezone.now(),
            end_time__lte=timezone.now() + timezone.timedelta(days=7)
        ).order_by('start_time')
