from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    occupations = (
        ("TP", "Traffic police"), 
        ("LP", "Local police"),
        ("DP", "Department of Highway"),
    )
    
    __occupation = models.CharField(max_length=2, choices=occupations)
    __phone_number = models.TextField()
    __bio = models.TextField(default=None, null=True, blank=True)

    def get_occupation(self):
        return self.__occupation

    def get_phone_number(self):
        return self.__phone_number
    
    def get_bio(self):
        return self.__bio
    
    def set_occupation(self, value):
        self.__occupation == value
    
    def set_phone_number(self, value):
        self.__phone_number == value

    def set_bio(self, value):
        self.__bio == value
