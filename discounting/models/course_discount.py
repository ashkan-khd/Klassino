from django.db import models

from discounting.models import Discount
from teaching.models import Course


class CourseDiscount(Discount):
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        verbose_name='دوره',
        related_name='discounts',
    )

    class Meta:
        verbose_name = 'تخفیف کلاس'
        verbose_name_plural = 'تخفیف های کلاس'

    def __str__(self):
        return str(self.percentage) + '% ' + " - (" + str(self.course) + ") - (" + str(self.student) + ")"
