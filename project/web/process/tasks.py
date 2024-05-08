import sys
sys.path.append('../ai')
from .functions import edit_status
from detect_and_track_ooad import Detection
from celery import shared_task

# from django.core.mail import send_mail
# from time import sleep

@shared_task()
def celery_start_task(url, id):
    edit_status(1, id)
    call_detect = Detection()
    call_detect.detect(url)
    edit_status(2, id)
    return "Detect Finish"