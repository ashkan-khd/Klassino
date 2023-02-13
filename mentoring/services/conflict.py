from django.db.models import Q


def has_conflict(student, start_time, end_time):
    return student.assigned_study_periods.filter(
        Q(end_time__gt=start_time, end_time__lt=end_time) |
        Q(start_time__gte=start_time, start_time__lt=end_time),
        is_deleted=False
    ).exists()
