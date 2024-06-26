from django.urls import path
from process import functions

urlpatterns = [
    # Create
    path('create_intersection/submit', functions.create_intersection, name='create_intersection'),
    path('upload_task/submit', functions.create_task, name='create_task'),
    path('edit_task/add_loop/<int:task_id>', functions.add_loop, name='add_loop'), 
    

    # Delete
    path('delete_task/<int:task_id>', functions.delete_task, name='delete_task'),
    path('delete_result/<int:result_id>', functions.delete_result, name='delete_result'),
    path('delete_intersection/<int:intersection_id>', functions.delete_intersection, name='delete_intersection'),
    path('delete_loop/<str:loop_id>', functions.delete_loop, name='delete_loop'),
    # submit
    path('submit_task/<str:task_id>', functions.submit_task, name='submit_task'),
    # test celery
    path('get_result/<str:task_id>', functions.get_result, name='get_result'),
    path('task_status/<str:task_id>/', functions.task_status, name='task_status'),
]
