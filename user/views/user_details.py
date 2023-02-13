from rest_framework import views, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.models import Student
from user.permissions import IsStudent, PasswordIsCorrect
from user.serializers import USER_DETAILS_SERIALIZER_MAP, StudentEditSerializer
from user.services import concrete


class UserDetailsView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        model_object = concrete(self.request.user)
        serializer_class = USER_DETAILS_SERIALIZER_MAP[type(model_object)]
        return Response(
            data=serializer_class(
                model_object,
                context={
                    'request': request
                }
            ).data
        )


class StudentEditDetailsView(viewsets.ModelViewSet):
    serializer_class = StudentEditSerializer
    permission_classes = [IsStudent]

    def get_permissions(self):
        if self.action == 'partial_update':
            return super().get_permissions() + [PasswordIsCorrect()]
        else:
            return super().get_permissions()

    def get_queryset(self):
        return Student.objects.filter(
            id=self.request.user.student.id
        )

    def get_object(self):
        return self.get_queryset().first()

