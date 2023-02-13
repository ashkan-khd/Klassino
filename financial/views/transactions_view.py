from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from financial.serializers.transaction_serializer import TransactionSerializer
from user.permissions import IsStudent


class TransactionsPagePaginator(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'


class TransactionView(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    authentication_classes = [TokenAuthentication]

    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [IsAuthenticated, IsStudent]
    pagination_class = TransactionsPagePaginator

    def get_queryset(self):
        return self.request.user.student.transactions.all().order_by('transaction_time')
