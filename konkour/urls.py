from django.urls import path

from konkour.views import KonkourDateView

urlpatterns = [
    path('get-date/', KonkourDateView.as_view())
]
