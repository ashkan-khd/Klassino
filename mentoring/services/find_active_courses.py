from django.db import models
from django.db.models import ExpressionWrapper, F
from django.db.models.functions import Cast
from django.utils import timezone

from mentoring.models import AssistanceCourse


def find_active_assistance_courses(queryset=None):
    if queryset is None:
        queryset = AssistanceCourse.active_objects.all()
    return queryset.annotate(
        end_time=ExpressionWrapper(
            Cast(F('created__date'), output_field=models.DateField()) + F('assistance_package__duration_days'),
            output_field=models.DateField()
        )
    ).filter(
        end_time__gte=timezone.now()
    )
