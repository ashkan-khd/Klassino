import requests
from django.db import models
from skyroom import SkyroomAPI

from karino import settings
from teaching.models import Subject
from user.models import Teacher


class Course(models.Model):
    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.PROTECT,
        related_name='courses',
        verbose_name='درس',
    )

    teacher = models.ForeignKey(
        to=Teacher,
        on_delete=models.PROTECT,
        related_name='courses',
        verbose_name='استاد',
    )

    price = models.PositiveBigIntegerField(
        verbose_name='قیمت'
    )

    start_time = models.DateField(
        verbose_name='تاریخ شروع دوره'
    )

    end_time = models.DateField(
        verbose_name='تاریخ پایان دوره'
    )

    skyroom_name = models.CharField(
        max_length=50,
        verbose_name='نام اتاق اسکای‌روم',
        help_text='این فیلد برای اینکه دانش‌آموزان بتوانند به کلاس وارد شوند الزامی‌است!',
    )

    @property
    def skyroom_id(self):
        api = SkyroomAPI(settings.SKYROOM['API_KEY'])
        result = api.getRoom(params={
            'name': self.skyroom_name
        })
        return result['id']

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره‌ها'

    def __str__(self):
        return '(' + str(self.subject) + ") - (" + str(self.teacher) + ')'
