from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from financial.models import Transaction
from teaching.models import Course, CourseSubscription
from user.permissions import IsStudent


class PurchaseCourseView(APIView):
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [IsAuthenticated, IsStudent]

    def post(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        student = request.user.student
        if course.start_time < timezone.localdate():
            raise ValidationError('این دوره به پایان رسیده است.')

        if course.subscriptions.filter(student=student).exists():
            raise ValidationError('شما قبلا این کلاس را خریداری کرده‌اید.')

        if student.balance < course.price:
            raise ValidationError('شما موجودی کافی ندارید.')

        with transaction.atomic():
            course_subscription = CourseSubscription.objects.create(
                course=course,
                student=student,
            )
            Transaction.objects.create(
                user=self.request.user.student,
                amount=-course.price,
                description='برای خرید دوره ی {}'.format(str(course)),
                transaction_time=timezone.now(),
                extra_data={
                    'course_subscription': course_subscription.id
                }
            )

        return Response(status=HTTP_201_CREATED)
