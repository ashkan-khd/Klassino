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
from mentoring.models import AssistancePackage, AssistanceCourse
from mentoring.services import find_active_assistance_courses
from user.permissions import IsStudent


class PurchasePackage(APIView):
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [IsAuthenticated, IsStudent]

    def post(self, request, package_id):
        package = get_object_or_404(AssistancePackage, id=package_id)
        student = request.user.student

        if find_active_assistance_courses(package.courses.filter(student=student)).exists():
            raise ValidationError('شما قبلا این دوره مشاوره را خریداری کرده‌اید.')

        if student.balance < package.price:
            raise ValidationError('شما موجودی کافی ندارید.')

        with transaction.atomic():
            assistance_course = AssistanceCourse.objects.create(
                assistance_package=package,
                student=student,
            )
            Transaction.objects.create(
                user=self.request.user.student,
                amount=-package.price,
                description='برای خرید دوره ی مشاوره ی {}'.format(str(package)),
                transaction_time=timezone.now(),
                extra_data={
                    'assistance_course': assistance_course.id
                }
            )

        return Response(status=HTTP_201_CREATED)
