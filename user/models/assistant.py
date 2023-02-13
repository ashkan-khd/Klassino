from django.db import models

from user.models.karino_user import KarinoUser
from utility.models import BaseModel


class Assistant(KarinoUser, BaseModel):
    description = models.TextField(
        verbose_name='توضیحات'
    )

    short_description = models.TextField(
        verbose_name='توضیحات کوتاه',
    )

    is_top = models.BooleanField(
        verbose_name='در برترین مشاورین باشد؟',
        default=False,
    )

    home_page_image = models.FileField(
        verbose_name='عکس صفحه اصلی',
        null=True,
        blank=True,
        help_text='اگر این فیلد خالی باشد عکس پروفایل در صفحه اصلی(در صورت در برترین مشاورین بودن) نمایش داده خواهد شد.'
    )

    class Meta:
        verbose_name = 'مشاور'
        verbose_name_plural = 'مشاوران'

    def __str__(self):
        return str(self.username) + ' - ' + str(self.first_name) + " " + str(self.last_name)
