from django.db import models

from financial.models import PrimeTransaction


class Transaction(PrimeTransaction):
    # Put Extra Fields Like Bank Receipts Here

    extra_data = models.JSONField(
        verbose_name='اطلاعات',
        default=dict
    )

    class Meta:
        verbose_name = 'تراکنش'
        verbose_name_plural = 'تراکنش ها'
