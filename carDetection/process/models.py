from django.db import models
from location_field.models.plain import PlainLocationField
# Use the built-in JSONField for compatibility with SQLite
from django.db.models import JSONField
from user.models import Profile

class Vehicle(models.Model):
    location = PlainLocationField(based_fields=['city'], zoom=7)
    speed = models.FloatField()
    color = models.TextField()
    license_plate = models.TextField()
    brand = models.TextField()
    
    # class Meta:
    #     abstract = True

class Car(Vehicle):
    model = models.TextField()

class Motorbike(Vehicle):
    model = models.TextField()

class Truck(Vehicle):
    model = models.TextField()

class Intersection(models.Model):
    intersection_name = models.CharField(max_length=256)
    location = PlainLocationField()

    def __str__(self):
        return self.intersection_name


class Road(models.Model):
    code = models.IntegerField()
    road_name = models.CharField(max_length=256)
    lanes = models.IntegerField()
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE)

class Task(models.Model):
    status = models.TextField()
    video = models.FileField(upload_to='static/video', blank=True, null=True)
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE)

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    result = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.task_id

class Loop(models.Model):
    loop_name = models.CharField(max_length=256)
    # Replace ArrayField with JSONField
    points = JSONField(default=list)  # Example: [[x1, y1], [x2, y2], ...]
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

class Result(models.Model):
    vehicle_count = models.IntegerField()
    # Replace ArrayField with JSONField for vehicle_with_direction
    vehicle_with_direction = JSONField(default=list)  # Example: [["Car", "North"], ["Truck", "South"], ...]

class Weather(models.Model):
    how = models.TextField()
