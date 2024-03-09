from django.urls import path
from . import views

urlpatterns = [
    path('create_task', views.view_create_task, name='view_create_task'),
    path('create_intersection', views.view_create_intersection, name='view_create_intersection'),
    path('edit_task/<int:task_id>', views.view_edit_task, name='view_edit_task'),
    path('display_result/<str:result_id>', views.view_display_result, name='view_result'),
    path('', views.process_view, name='process_view'),
]
