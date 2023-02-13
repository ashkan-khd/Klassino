from django.db import models

from discounting.models import Discount
from mentoring.models import AssistancePackage


class AssistanceDiscount(Discount):
    assistance = models.ForeignKey(
        to=AssistancePackage,
        on_delete=models.CASCADE,
        verbose_name='مشاوره',
        related_name='discounts'
    )

    class Meta:
        verbose_name = 'تخفیف مشاوره'
        verbose_name_plural = 'تخفیف های مشاوره'

    def __str__(self):
        return str(self.percentage) + '% ' + " - (" + str(self.assistance) + ") - (" + str(self.student) + ")"
