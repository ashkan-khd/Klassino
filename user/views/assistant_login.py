from django.contrib.auth.hashers import check_password
from rest_framework import views
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN, HTTP_200_OK

from user.models import Assistant
from user.serializers import AssistantLoginSerializer
from user.services.authentication import get_or_create_token


class AssistantLoginView(views.APIView):
    def post(self, request):
        serializer = AssistantLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        username, password = data.get('username', ''), data.get('password', '')
        assistant = get_object_or_404(Assistant.active_objects.all(), username=username)

        if not check_password(password, assistant.password):
            raise ValidationError(
                'پسورد اشتباه است', code=HTTP_403_FORBIDDEN
            )

        token = get_or_create_token(assistant)
        return Response(
            data={
                'auth_token': token.key
            },
            status=HTTP_200_OK
        )
