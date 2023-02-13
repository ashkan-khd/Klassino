from django.contrib.auth.hashers import check_password
from rest_framework import views
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN, HTTP_200_OK

from user.models import Student
from user.serializers import LoginSerializer
from user.services.authentication import get_or_create_token


class LoginView(views.APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        nationality_code, password = data.get('nationality_code', ''), data.get('password', '')
        student = get_object_or_404(Student.active_objects.all(), nationality_code=nationality_code)

        if not check_password(password, student.password):
            raise ValidationError(
                'پسورد اشتباه است', code=HTTP_403_FORBIDDEN
            )

        token = get_or_create_token(student)
        return Response(
            data={
                'auth_token': token.key
            },
            status=HTTP_200_OK
        )
