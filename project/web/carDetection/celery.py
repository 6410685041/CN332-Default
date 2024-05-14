from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carDetection.settings')

app = Celery('carDetection', 
             backend='rpc://', # RabbitMQ
             broker='amqp://',
             include=['process.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()