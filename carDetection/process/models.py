from django.db import models
from location_field.models.plain import PlainLocationField
from django.contrib.postgres.fields import ArrayField

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
    
class Intersection(models.Model):
    intersection_name = models.CharField(max_length=256)
    location = PlainLocationField()
    
class Road(models.Model):
    code = models.IntegerField()
    road_name = models.CharField(max_length=256)
    lanes = models.IntegerField()
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE)

class Task(models.Model):
    status = models.TextField()
    time = models.DateTimeField()
    video = models.FileField(upload_to='video_file', blank=True, null=True)
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE)
    

class Loop(models.Model):
    loop_name = models.CharField(max_length=256)
    points = ArrayField(
        ArrayField(
            models.FloatField(blank=True),
            size=2,
        ),
        size=4,
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

class Result(models.Model):
    vehicle_count = models.IntegerField()
    vehicle_with_direction = ArrayField(
        ArrayField(
            models.CharField(max_length=256),
        ),   
    )
