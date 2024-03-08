from django.urls import path
from . import views

urlpatterns = [
    # view
    path('create_task', views.view_create_task, name='create_task'),
    path('create_intersection', views.view_create_intersection, name='create_intersection'),
    path('edit_task/<int:task_id>', views.view_edit_task, name='edit_task'),
    path('display_result/<str:result_id>', views.view_display_result, name='display_result'),
    # create
    path('create_intersection/submit', views.create_intersection, name='submit_intersection'),
    path('upload_task/submit', views.create_task, name='upload_video'),
    path('edit_task/add_loop/<int:task_id>', views.add_loop, name='add_loop'),
    # delete
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('delete_result/<int:result_id>', views.delete_result, name='delete_result'),
    path('delete_intersection/<int:intersection_id>', views.delete_intersection, name='delete_intersection'),
    # submit
    path('submit_task/<int:task_id>', views.submit_task, name='submit_task'),
    # test celery
    path('', views.process_view, name='process_view'),
    path('start-task/', views.start_task, name='start-task'),
    path('task-status/<str:task_id>/', views.task_status, name='task-status'),
]
