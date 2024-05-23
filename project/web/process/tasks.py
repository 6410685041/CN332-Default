# tasks.py
from celery import shared_task
import requests
from requests.exceptions import RequestException

@shared_task(bind=True, max_retries=5, default_retry_delay=10)
def celery_start_task(self, loop, source, task_id):
    url = 'http://ai_service:80/run-task'
    data = {
        'loop': loop,
        'source': source,
        'task_id': task_id
    }
    print(f"Sending POST request to {url} with data: {data}")
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Ensure we raise an exception for bad status codes
        print("Connection successful: ", response.text)
        return response.text  # Assuming the response is plain text
    except RequestException as exc:
        print("Connection failed: ", exc)
        raise self.retry(exc=exc)

@shared_task()
def add(x, y):
    return x + y