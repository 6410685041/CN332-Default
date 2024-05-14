import os
import sys
# Assuming 'detect_and_track_ooad' module is one directory above the current directory
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ai')))


# from .functions import edit_status
# from web.ai.detect_and_track_ooad import Detection
from celery import shared_task

# from django.core.mail import send_mail
# from time import sleep

@shared_task()
def celery_start_task(url):
    # edit_status(1, id)
    call_detect = Detection()
    call_detect.detect(url)
    # edit_status(2, id)
    return "Detect Finish"

@shared_task()
def add(x, y):
    return x+y