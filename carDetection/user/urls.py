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

from django.urls import path, include  # social
from . import views

urlpatterns = [
    path('profile', views.view_profile, name='profile'),
    path('my_queue', views.view_my_queue, name='my_queue'),
    path('edit_profile', views.view_edit_profile, name='edit_profile'),
    path('edit_profile/submit', views.submit_edit_profile, name='submit_profile'),
]
