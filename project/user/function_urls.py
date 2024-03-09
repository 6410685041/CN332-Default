from django.urls import path
from . import functions

urlpatterns = [
    path('edit_profile/submit', functions.edit_profile, name='edit_profile'),
]