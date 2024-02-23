from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.

class Vehicle(models.Model):
    location = PlainLocationField(based_fields=['city'], zoom=7)
    speed = models.FloatField()
    color = models.TextField()
    license_plate = models.TextField()
    brand = models.TextField()
    class Meta:
        abstract = True
        
class Car(Vehicle):
    model = models.TextField()

class Motorbike(Vehicle):
    model = models.TextField()
    
class Truck(Vehicle):
    model = models.TextField()
    
    
class Road(models.Model):
    code = models.IntegerField()
    road_name = models.CharField(max_length=256)
    lanes = models.IntegerField()
    
class Intersection(models.Model):
    intersection_name = models.CharField(max_length=256)
    location = PlainLocationField()
    roads = models.ForeignKey(Road, verbose_name="road", on_delete=models.CASCADE)