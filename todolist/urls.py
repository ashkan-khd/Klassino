from django.urls import path
from todolist.views import ToDoUserView

urlpatterns = [
    path(
        'todo_list/user/',
        ToDoUserView.as_view({
            'get': 'list',
            'post': 'create',
        })
    ),
    path(
        'todo_list/user/<int:pk>/',
        ToDoUserView.as_view({
            'delete': 'destroy',
            'post': 'update'
        })
    )
]
