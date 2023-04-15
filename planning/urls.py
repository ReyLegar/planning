from django.urls import path
from plan.controller import task_list, add_task, change_status, delete_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('<int:pk>/change-status/', change_status, name='change_status'),
    path('delete_task/<int:pk>/', delete_task, name='delete_task'),

]
