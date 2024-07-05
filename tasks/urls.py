from django.urls import path
from .views import list_tasks, create_task, delete_task, edit_task, task_completed

urlpatterns = [
    path('', list_tasks),
    path('new/', create_task, name='create_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('completed/<int:task_id>/', task_completed, name='task_completed')
]