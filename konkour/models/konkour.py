from django.db import models

from konkour.enums import FIELD_CHOICES


class Konkour(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='نام کنکور',
        unique=True,
    )

    date = models.DateTimeField(
        verbose_name='تاریخ برگزاری'
    )

    field = models.CharField(
        max_length=20,
        choices=FIELD_CHOICES,
        verbose_name='رشته'
    )

    class Meta:
        verbose_name = 'کنکور'
        verbose_name_plural = 'کنکورها'

    def __str__(self):
        return str(self.name) + ' --- ' + str(self.date)
