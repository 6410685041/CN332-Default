from django.shortcuts import render
from django.urls import reverse
from process.models import Task, Intersection, Result,Loop
from django.http import HttpResponseRedirect
from celery.result import AsyncResult
from process import functions
import json
from django.contrib.auth.decorators import login_required

'''
render
'''

# test celery
def process_view(request):
    # Example list of task IDs you might be tracking
    tracked_tasks = Task.objects.all().order_by('created_at')  # Get all tasks, newest first
    tasks = []

    for tracked_task in tracked_tasks:
        result = AsyncResult(tracked_task.id)
        tasks.append({
            'id': tracked_task,
            'status': result.status,
            'result': result.result if result.ready() else 'N/A',
        })
    return render(request, "process/process_view.html", {'tasks': tracked_tasks})


# go to upload page (for upload video)
@login_required
def view_create_task(request):
    intersections = Intersection.objects.all()
    data = {"intersections": intersections}
    return render(request, "process/create_task.html", data)

# view edit task
@login_required
def view_edit_task(request, task_id):
    loops = Loop.objects.filter(task_id=task_id)
    loop_id = request.session.pop('loop_id', None)
    task = Task.objects.get(id=task_id)
    data = {
        "task": task,
        "loop_id": loop_id,
        "loops": loops,
    }
    return render(request, "process/edit_task.html", data)

# view result
@login_required
def view_display_result(request, result_id):
    result = Result.objects.get(id=result_id)
    loop_path = result.loop_json
    summary_path = functions.create_summary(result_id, loop_path)
    with open(summary_path, 'r') as file:
            json_data = file.read()
            summary = json.loads(json_data)
    data = {
        'result': result,
        'summary': summary,
    }
    return render(request, "process/result.html", data)


@login_required
def view_create_intersection(request):
    intersections = Intersection.objects.all()
    data = {
            "intersections" : intersections,
    }
    return render(request, "process/create_intersection.html", data)