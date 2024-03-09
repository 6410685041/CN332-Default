from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.view_profile, name='profile'),
    path('my_queue', views.view_my_queue, name='my_queue'),
    path('edit_profile', views.view_edit_profile, name='view_edit_profile'),
]
