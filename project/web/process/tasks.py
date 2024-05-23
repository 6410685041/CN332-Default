# tasks.py
from celery import shared_task

@shared_task
def celery_start_task(data):
    url = 'http://ai_service:80/run-task'
    response = request.post(url, json=data)
    return response.json()

@shared_task()
def add(x, y):
    return x + y