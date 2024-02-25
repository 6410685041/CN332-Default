# myapp/tasks.py
from celery import shared_task
import time

@shared_task
def abc(x, y):
    for i in range(1000000):
        for i in range(1000000):
            for i in range(1000000):
                for i in range(1000000):
                    z = x*y*i
    return z