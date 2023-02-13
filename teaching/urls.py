from django.urls import path, include
from rest_framework.routers import DefaultRouter

from teaching.views import ActiveSubjectsView, PurchaseCourseView
from teaching.views.course_page import CoursePageView, CourseSessionView
from teaching.views.new_filtering import CourseListView
from teaching.views.my_desk_classes import MyDeskClassesViewSet

router = DefaultRouter()
router.register(r'course', CoursePageView)

get_to_list = {
    'get': 'list'
}

urlpatterns = [
    path('', include(router.urls)),
    path('session/', CourseSessionView.as_view(get_to_list)),
    path('subjects/', ActiveSubjectsView.as_view(get_to_list)),
    path('filtering/v2/', CourseListView.as_view()),
    path('get-desk-classes/', MyDeskClassesViewSet.as_view(get_to_list)),
    path('purchase_course/<int:course_id>/', PurchaseCourseView.as_view()),
]
