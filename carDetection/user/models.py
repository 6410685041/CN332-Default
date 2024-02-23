from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Profile(AbstractUser):
    occupations = {
        "TP": "Traffic police", 
        "LP": "Local police",
        "DP": "Department of Highway",
        }
    
    occupation = models.CharField(max_length=256, choices=occupations)
    phone_number = models.TextField()
    bio = models.TextField(default=None)

