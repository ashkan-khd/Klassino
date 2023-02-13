from django.utils import timezone
from rest_framework import views
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK

from konkour.services.konkour_api import get_closest_ahead_konkour


class KonkourDateView(views.APIView):
    def get(self, request):
        current_date = timezone.now()

        konkour = get_closest_ahead_konkour(current_date)
        if konkour is None:
            raise NotFound(
                'تاریخ کنکور بعدی مشخص نیست', code=HTTP_404_NOT_FOUND
            )

        return Response(
            data={
                'date': konkour.date
            },
            status=HTTP_200_OK
        )
