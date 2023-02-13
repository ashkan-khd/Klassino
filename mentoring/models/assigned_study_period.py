from django.db import models

from utility.models import BaseModel


class AssignedStudyPeriod(BaseModel):
    title = models.CharField(
        max_length=100,
        verbose_name='عنوان'
    )

    student = models.ForeignKey(
        to='user.Student',
        on_delete=models.CASCADE,
        related_name='assigned_study_periods',
        verbose_name='دانش‌آموز'
    )

    assistant = models.ForeignKey(
        to='user.Assistant',
        on_delete=models.CASCADE,
        related_name='assigned_by_study_periods',
        verbose_name='مشاور'
    )

    start_time = models.DateTimeField(
        verbose_name='تاریخ شروع'
    )

    end_time = models.DateTimeField(
        verbose_name='تاریخ پایان'
    )

    description = models.TextField(
        verbose_name='توضیحات'
    )

    class Meta:
        verbose_name = 'زمان مطالعه'
        verbose_name_plural = 'زمان‌های مطالعه'

    def __str__(self):
        return str(self.student) + " - " + str(self.assistant) + " / " + str(self.title)
