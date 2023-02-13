from django.urls import path

from announcement.views import AnnouncementViewSet

urlpatterns = [
    path('', AnnouncementViewSet.as_view({
        'get': 'list'
    }))
]
