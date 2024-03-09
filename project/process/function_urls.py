from django.urls import path
from . import functions

urlpatterns = [
    # Create
    path('create_intersection/submit', functions.create_intersection, name='create_intersection'),
    path('upload_task/submit', functions.create_task, name='create_task'),
    path('edit_task/add_loop/<int:task_id>', functions.add_loop, name='add_loop'), # not working

    # Delete
    path('delete_task/<int:task_id>', functions.delete_task, name='delete_task'),
    path('delete_result/<int:result_id>', functions.delete_result, name='delete_result'),
    path('delete_intersection/<int:intersection_id>', functions.delete_intersection, name='delete_intersection'),
    # submit
    path('submit_task/<int:task_id>', functions.submit_task, name='submit_task'), # not working
    # test celery
    path('start-task/', functions.start_task, name='start-task'),
    path('task-status/<str:task_id>/', functions.task_status, name='task-status'),
]
