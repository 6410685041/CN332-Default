import os
import sys
# Assuming 'detect_and_track_ooad' module is one directory above the current directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


# from .functions import edit_status
from ai.detect_and_track import mymain
from celery import shared_task

# from django.core.mail import send_mail
# from time import sleep

@shared_task
def celery_start_task(loopfile, vdofile):
    saved_result = mymain(cmd=False,custom_arg=['--loop',loopfile,'--source',vdofile])
    
    return saved_result

# @shared_task()
# def add(x, y):
#     return x+y