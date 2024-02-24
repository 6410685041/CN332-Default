"""
URL configuration for carDetection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('upload_task', views.view_upload_task, name='upload_task'),
    path('edit_task/<str:task_id>', views.view_edit_task, name='edit_task'),
    path('edit_task/add_loop/<str:task_id>', views.add_loop, name='add_loop'),
    path('submit_task/<str:task_id>', views.submit_task, name='submit_task'),
    path('display_result/<str:result_id>', views.view_display_result, name='display_result'),
    # test celery
    path('', views.process_view, name='process_view'),
    path('start-task/', views.start_task, name='start-task'),
    path('task-status/<str:task_id>/', views.task_status, name='task-status'),
]
