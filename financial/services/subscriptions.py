from django.utils import timezone

from mentoring.models import AssistanceCourse
from teaching.models import CourseSubscription


def create_course_subscription(course, transaction):
    CourseSubscription.objects.create(course=course, transaction=transaction)


def create_assistance_course(assistance_package, transaction):
    AssistanceCourse.objects.create(transaction=transaction, assistance_package=assistance_package)
