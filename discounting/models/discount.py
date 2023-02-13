from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from user.models import Student
from utility.models import BaseModel


class Discount(BaseModel):
    student = models.ForeignKey(
        to=Student,
        on_delete=models.CASCADE,
        verbose_name='گیرنده کد تخفیف',
    )

    code = models.CharField(max_length=20, verbose_name='کد', blank=True, unique=True)
    percentage = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],
                                     verbose_name='درصد تخفیف')

    start_time = models.DateTimeField(verbose_name='زمان شروع', default=timezone.now)
    end_time = models.DateTimeField(verbose_name='زمان پایان', )

    is_used = models.BooleanField(verbose_name='استفاده شده؟', default=False)

    class Meta:
        abstract: True

    def __str__(self):
        return str(self.percentage) + " - " + str(self.student)
