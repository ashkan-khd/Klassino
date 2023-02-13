from django.contrib.auth.models import User
from django.db import models


class KarinoUser(User):
    profile_image = models.FileField(
        verbose_name='عکس پروفایل',
        null=True,
        blank=True
    )

    phone_number = models.CharField(
        max_length=20,
        verbose_name='شماره تلفن'
    )

    class Meta:
        abstract = True
