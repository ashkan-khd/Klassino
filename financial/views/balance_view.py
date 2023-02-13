from rest_framework import views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings

from user.permissions import IsStudent


class BalanceView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [IsAuthenticated, IsStudent]

    def get(self, request):
        return Response(data={
            'balance': request.user.student.balance
        })
