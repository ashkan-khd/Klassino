from django.db import models

from utility.models import BaseModel


class SessionAttendance(BaseModel):
    skyroom_login_url = models.CharField(max_length=1024)
    subscription = models.ForeignKey(
        to='teaching.CourseSubscription',
        on_delete=models.CASCADE,
        related_name='attendances'
    )
    session = models.ForeignKey(
        to='teaching.CourseSession',
        on_delete=models.CASCADE,
        related_name='attendances'
    )
