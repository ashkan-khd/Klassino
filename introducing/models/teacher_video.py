from django.db import models

from user.models import Teacher


class TeacherIntroductionVideo(models.Model):
    teacher = models.ForeignKey(
        to=Teacher,
        on_delete=models.CASCADE,
        verbose_name='استاد',
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
        verbose_name = 'فیلم معرفی استاد'
        verbose_name_plural = 'فیلم‌های معرفی استاد'

    def __str__(self):
        return " :فیلم" + str(self.teacher)
