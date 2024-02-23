from django.db import models
from django.contrib.auth.models import User

# Create your models here.

occupations = ["Traffic police", "Local police", "Department police"]

class User(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE) 
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()

class Profile(User):
    occupation = models.CharField(choices=occupations)
    phone_number = models.TextField()
    bio = models.TextField(default=None)

