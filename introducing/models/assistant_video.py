from django.db import models

from user.models import Assistant


class AssistantIntroductionVideo(models.Model):
    assistant = models.ForeignKey(
        to=Assistant,
        on_delete=models.CASCADE,
        verbose_name='مشاور',
        related_name='introduction_videos'
    )

    aparat_id = models.CharField(
        max_length=20,
        verbose_name='آیدی آپارات'
    )

    embed_hash = models.CharField(
        max_length=10,
        verbose_name='هش ویدیو'
    )

    class Meta:
        verbose_name = 'فیلم معرفی مشاور'
        verbose_name_plural = 'فیلم‌های معرفی مشاور'

    def __str__(self):
        return " :فیلم" + str(self.assistant)
