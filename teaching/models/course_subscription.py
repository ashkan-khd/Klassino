from django.db import models
from django.db.models import CASCADE

from financial.models.transaction import Transaction
from teaching.models import Course


class CourseSubscription(models.Model):
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        verbose_name='کلاس خریداری شده',
        related_name='subscriptions',
    )

    student = models.ForeignKey(
        to="user.Student",
        on_delete=models.CASCADE,
        verbose_name='خریدار کلاس',
        related_name='courses',
    )

    class Meta:
        verbose_name = 'عضویت کلاس'
        verbose_name_plural = 'عضویت های کلاس'

    def __str__(self):
        return str(self.student) + " - " + str(self.course)
