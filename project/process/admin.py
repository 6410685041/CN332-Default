from django.contrib import admin

from .models import Car, Motorbike, Truck, Intersection, Road, Task, Loop, Result, Weather
# Register your models here.

admin.site.register(Car)
admin.site.register(Motorbike)
admin.site.register(Truck)
admin.site.register(Intersection)
admin.site.register(Road)
admin.site.register(Task)
admin.site.register(Loop)
admin.site.register(Result)
admin.site.register(Weather)