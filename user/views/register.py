from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from user.serializers import StudentRegisterSerializer
from user.services.authentication import get_or_create_token


class RegisterView(views.APIView):
    def post(self, request):
        serializer = StudentRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()

        token = get_or_create_token(student)

        return Response(
            data={
                'auth_token': token.key
            },
            status=HTTP_201_CREATED
        )
