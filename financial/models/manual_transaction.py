from financial.models import PrimeTransaction


class ManualTransaction(PrimeTransaction):

    class Meta:
        verbose_name = 'تراکنش دستی'
        verbose_name_plural = 'تراکنش های دستی'
