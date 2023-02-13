from django.db import models
from django.db.models import PROTECT

from user.models import Student
from utility.models import BaseModel


class PrimeTransaction(BaseModel):
    user = models.ForeignKey(
        to=Student,
        related_name='transactions',
        verbose_name='تراکنشگر',
        on_delete=PROTECT
    )

    amount = models.BigIntegerField(
        verbose_name='مبلغ تراکنش'
    )

    description = models.TextField(
        verbose_name='توضیحات تراکنش'
    )

    transaction_time = models.DateTimeField(
        verbose_name='تاریخ تراکنش'
    )

    def __str__(self):
        return '(' + str(self.amount) + " تومان) - (" + str(self.user) + ')'

    class Meta:
        abstract: True
