from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    occupations = (
        ("TP", "Traffic police"), 
        ("LP", "Local police"),
        ("DP", "Department of Highway"),
    )
    
    occupation = models.CharField(max_length=2, choices=occupations)
    phone_number = models.TextField()
    bio = models.TextField(default=None, null=True, blank=True)
