from django.urls import path

from financial.views import TransactionView,BalanceView

urlpatterns = [
    path(
        'transactions/',
        TransactionView.as_view({'get': 'list'})
    ),
    path(
        'balance/',
        BalanceView.as_view()
    )
]