from django.db import models

from teaching.enums import GRADE_CHOICES


class Subject(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='نام درس'
    )

    grade = models.CharField(
        max_length=15,
        choices=GRADE_CHOICES,
        verbose_name='پایه'
    )

    def __str__(self):
        return self.name + ' - ' + self.grade

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'درس‌ها'


