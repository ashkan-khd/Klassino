import datetime

from django.utils import timezone, dateparse
from django.utils.timezone import make_aware, is_aware
from jalali_date import datetime2jalali
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from user.permissions import IsStudent, IsAssistant
from todolist.serializers import TodoSerializer, NewTodoSerializer


class ToDoUserView(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TodoSerializer
        else:
            return NewTodoSerializer

    authentication_classes = [TokenAuthentication]

    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [IsAuthenticated, IsStudent | IsAssistant]

    def get_queryset(self):
        return self.request.user.todo_items.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
