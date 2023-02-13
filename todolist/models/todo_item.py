from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class TodoItem(models.Model):

    todo = models.CharField(
        max_length=300,
        verbose_name='عنوان برنامه'
    )

    complete = models.BooleanField(
        verbose_name='انجام شده',
        default=False
    )

    user = models.ForeignKey(
        to=User,
        related_name='todo_items',
        verbose_name='کاربر',
        on_delete=CASCADE
    )