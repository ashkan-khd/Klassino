from django.urls import path

from mentoring.views import AssistancePackageView, AssignedStudyPeriodStudentView, AssignedStudyPeriodAssistantView, \
    MentoredStudentsViewSet, PurchasePackage, MyAssistants

urlpatterns = [
    path(
        'assistance_package/<str:lookup>/',
        AssistancePackageView.as_view({
            'get': 'retrieve'
        })
    ),
    path(
        'assigned_study_period/',
        AssignedStudyPeriodStudentView.as_view({
            'get': 'list'
        })
    ),
    path(
        'assigned_study_period/assistant/', AssignedStudyPeriodAssistantView.as_view({
            'post': 'create',
            'get': 'list',
        })
    ),
    path(
        'assigned_study_period/assistant/<int:pk>/',
        AssignedStudyPeriodAssistantView.as_view({
            'delete': 'destroy'
        })
    ),
    path('students/', MentoredStudentsViewSet.as_view({
        'get': 'list'
    })),
    path('purchase_package/<int:package_id>/', PurchasePackage.as_view()),
    path('my_assistants/', MyAssistants.as_view({'get': 'list'})),
]
