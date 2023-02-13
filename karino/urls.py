from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls')),
    path('mentoring/', include('mentoring.urls')),
    path('introduction/', include('introducing.urls')),
    path('teaching/', include('teaching.urls')),
    path('konkour/', include('konkour.urls')),
    path('announcement/', include('announcement.urls')),
    path('todolist/', include('todolist.urls')),
    path('financial/', include('financial.urls')),
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
