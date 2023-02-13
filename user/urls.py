from django.urls import path

from user.views import RegisterView, StatesListView, LoginView, StateCitiesView, UserDetailsView, AssistantLoginView, \
    TopAssistantViewSet, TopTeacherViewSet, AssistantViewSet, StudentEditDetailsView

urlpatterns = [
    path('assistants/', AssistantViewSet.as_view({'get': 'list'})),
    path('assistants/<int:pk>/', AssistantViewSet.as_view({'get': 'retrieve'})),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('assistant_login/', AssistantLoginView.as_view()),
    path('states/', StatesListView.as_view({
        'get': 'list'
    })),
    path('states/<int:pk>/', StateCitiesView.as_view({
        'get': 'retrieve'
    })),
    path('details/', UserDetailsView.as_view()),
    path('top_assistants/', TopAssistantViewSet.as_view({
        'get': 'list'
    })),
    path('top_teachers/', TopTeacherViewSet.as_view({
        'get': 'list'
    })),
    path('student_profile/', StudentEditDetailsView.as_view({
        'get': 'retrieve',
        'patch': 'partial_update'
    })),
]
