from django.db import models
from location_field.models.plain import PlainLocationField
from django.db.models import JSONField
from user.models import Profile

class myVehicle(models.Model):
    location = PlainLocationField(based_fields=['city'], zoom=7)
    speed = models.FloatField()
    color = models.TextField()
    license_plate = models.TextField()
    brand = models.TextField()
    
    class Meta:
        app_label = 'process'
    # class Meta:
    #     abstract = True

class Car(myVehicle):
    model = models.TextField()

class Motorbike(myVehicle):
    model = models.TextField()

class Truck(myVehicle):
    model = models.TextField()

class Intersection(models.Model):
    intersection_name = models.CharField(max_length=256, null=False, blank=False)
    location = PlainLocationField(null=False, blank=False)

    def __str__(self):
        return self.intersection_name


class Road(models.Model):
    code = models.IntegerField()
    road_name = models.CharField(max_length=256)
    lanes = models.IntegerField()
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE)

class Task(models.Model):
    task_name = models.TextField()
    status = models.TextField()
    video = models.FileField(upload_to="static/video/", blank=False, null=False)
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE)

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    result = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.task_name)

class Loop(models.Model):
    points = JSONField(default=list)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

class Result(models.Model):
    result_name = models.TextField()
    video = models.FileField(blank=False, null=False)
    intersection = models.TextField()
    owner = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    loop_json = JSONField(default=list)
    result_json = JSONField(default=list)

    def __str__(self):
        return str(self.result_name)


class Weather(models.Model):
    how = models.TextField()
