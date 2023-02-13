import logging

from django.db import models
from django.utils import timezone
from skyroom import SkyroomAPI

from karino import settings
from teaching.models import Course

logger = logging.getLogger(__name__)


class CourseSession(models.Model):
    start_time = models.DateTimeField(
        verbose_name='زمان شروع جلسه'
    )

    end_time = models.DateTimeField(
        verbose_name='زمان پایان جلسه'
    )

    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        verbose_name='کلاس',
        related_name='sessions',
    )

    def try_generate_login_url(self, student):
        api = SkyroomAPI(settings.SKYROOM['API_KEY'])
        try:
            result = api._request(action='createLoginUrl', params={
                'room_id': self.course.skyroom_id,
                'user_id': student.id,
                'nickname': student.get_full_name(),
                'access': 1,
                'concurrent': 1,
                'language': 'fa',
                'ttl': (self.course.end_time - self.course.start_time + timezone.timedelta(
                    minutes=15)) // timezone.timedelta(seconds=1),
            })
            return result
        except Exception as e:
            logger.error('Failed with skyroom')
            return None

    def generate_login_url(self, student):
        subscription = self.course.subscriptions.filter(student=student).first()
        attendance = subscription.attendances.filter(session=self, is_deleted=False).first()
        if attendance is not None:
            return attendance.skyroom_login_url
        retry_count = settings.SKYROOM.get('retry_count', 3)
        while retry_count:
            retry_count -= 1
            data = self.try_generate_login_url(student)
            if data:
                attendance = subscription.attendances.create(
                    skyroom_login_url=data,
                    session=self,
                )
                return attendance.skyroom_login_url
            else:
                logger.error('Failed in skyroom', exc_info=True, extra={
                    'response': data
                })
        return None

    class Meta:
        verbose_name = 'جلسه ی کلاس'
        verbose_name_plural = 'جلسه‌های کلاس'

    def __str__(self):
        return str(self.course)
