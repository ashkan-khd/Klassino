from django.db import models


STUDENTS_PAGE = 'صفحه دانش آموزان'
MAIN_PAGE = 'صفحه اصلی'
ANNOUNCEMENT_CHOICES = [
    (STUDENTS_PAGE, 'صفحه دانش آموزان'),
    (MAIN_PAGE, 'صفحه اصلی'),
]


class Announcement(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ایجاد'
    )

    title = models.CharField(
        max_length=50,
        verbose_name='موضوع',
    )
    context = models.TextField(
        verbose_name='متن اطلاعیه'
    )

    student_page = models.BooleanField(
        verbose_name='در پنل دانش آموزان نشان داده شود؟'
    )
    main_page = models.BooleanField(
        verbose_name='در صفحه اصلی نشان داده شود؟'
    )

    class Meta:
        verbose_name = 'اطلاعیه'
        verbose_name_plural = 'اطلاعیه ها'

    def __str__(self):
        return self.title
