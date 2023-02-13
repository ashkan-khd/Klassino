from django.db import models
from django.db.models import CASCADE
from user.models import State


class City(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='شهز'
    )

    state = models.ForeignKey(
        to=State,
        related_name='cities',
        verbose_name='استان',
        on_delete=CASCADE
    )

    def __str__(self):
        return str(self.name) + ' --- ' + str(self.state)

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهرها'
