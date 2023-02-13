from django.db import models

from user.models import Assistant
from utility.models import BaseModel


class AssistancePackage(BaseModel):
    assistant = models.ForeignKey(
        to=Assistant,
        on_delete=models.PROTECT,
        verbose_name='مشاور',
        related_name='packages'
    )

    price = models.PositiveBigIntegerField(
        verbose_name='قیمت'
    )

    duration_days = models.PositiveIntegerField(
        verbose_name='مدت دوره به روز'
    )

    description = models.TextField(
        verbose_name='معرفی بسته مشاوره'
    )

    class Meta:
        verbose_name = 'بسته ی مشاوره'
        verbose_name_plural = 'بسته‌های مشاوره'

    def __str__(self):
        return "("+str(self.assistant) + ") - (" + str(self.duration_days) + " روز" + ")"
