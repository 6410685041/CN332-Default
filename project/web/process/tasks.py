# tasks.py

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from celery import shared_task
from ai.detect_and_track import mymain

@shared_task
def celery_start_task(loop, source, filename):
    saved_result = mymain(cmd=False, custom_arg=['--loop', loop, '--source', source, '--filename', filename])
    return saved_result
    # pass

@shared_task()
def add(x, y):
    return x + y