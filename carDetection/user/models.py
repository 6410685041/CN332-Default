from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class Profile(AbstractUser):
    occupations = (
        ("TP", "Traffic police"), 
        ("LP", "Local police"),
        ("DP", "Department of Highway"),
    )
    
    occupation = models.CharField(max_length=2, choices=occupations)
    phone_number = PhoneNumberField(blank=True, null=True)
    bio = models.TextField(default=None, null=True, blank=True)
