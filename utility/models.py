from django.db import models
from simple_history.models import HistoricalRecords


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    history = HistoricalRecords(inherit=True)

    objects = models.Manager()
    active_objects = ActiveManager()

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ایجاد',
    )

    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='تاریخ آخرین ویرایش'
    )

    is_deleted = models.BooleanField(
        default=False,
        verbose_name='آیا حذف شده است؟'
    )

    @property
    def meta(self):
        return self._meta

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
