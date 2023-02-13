from django.urls import path, include

from introducing.views import VideosViewSet

urlpatterns = [
    path('<int:user_id>/', VideosViewSet.as_view({
        'get': 'list',
    }))
]
