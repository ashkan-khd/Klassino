from django.db import models
from django.db.models import PROTECT, Sum

from user.models import City
from user.models.karino_user import KarinoUser
from utility.models import BaseModel


class Student(KarinoUser, BaseModel):
    nationality_code = models.CharField(
        max_length=10,
        verbose_name='شماره شناسنامه',
        unique=True
    )

    birth_date = models.DateField(
        verbose_name='تاریخ تولد'
    )

    GENDER_CHOICE = (
        ('female', 'زن'),
        ('male', 'مرد'),
    )

    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICE,
        verbose_name='جنسیت',
        default='female'
    )

    school = models.CharField(
        max_length=50,
        verbose_name='مدرسه'
    )

    city = models.ForeignKey(
        to=City,
        related_name='students',
        verbose_name='شهر',
        on_delete=PROTECT,
        null=True
    )

    def save(self, *args, **kwargs):
        self.username = self.nationality_code
        super().save()

    class Meta:
        verbose_name = 'دانش‌آموز'
        verbose_name_plural = 'دانش‌آموزان'

    @property
    def balance(self):
        return self.transactions.all().aggregate(balance=Sum('amount'))['balance'] or 0

    def __str__(self):
        return str(self.nationality_code) + ' - ' + str(self.first_name) + ' ' + str(self.last_name)
