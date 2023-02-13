from django.db import models
from django.db.models import CASCADE

from financial.models.transaction import Transaction
from mentoring.models import AssistancePackage
from user.models import Student
from utility.models import BaseModel


class AssistanceCourse(BaseModel):

    student = models.ForeignKey(
        to=Student,
        verbose_name='دانش‌آموز',
        on_delete=models.CASCADE,
        related_name='assistance_courses'
    )

    assistance_package = models.ForeignKey(
        to=AssistancePackage,
        on_delete=models.CASCADE,
        verbose_name='بسته ی مشاوره',
        related_name='courses'
    )

    class Meta:
        verbose_name = 'دوره ی مشاوره'
        verbose_name_plural = 'دوره‌های مشاوره'

    def __str__(self):
        return '(' + str(self.student) + ") - (" + str(self.assistance_package) + ')'
