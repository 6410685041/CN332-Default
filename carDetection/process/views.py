from django.shortcuts import render
from django.urls import reverse
from process.models import Task, Intersection, Loop, Result
from django.http import HttpResponseRedirect, JsonResponse
from celery.result import AsyncResult

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
def view_create_task(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    intersections = Intersection.objects.all()
    data = {"intersections": intersections}
    return render(request, "process/create_task.html", data)

# view edit task
def view_edit_task(request, task_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    task = Task.objects.get(id=task_id)
    data = {
        "task": task,
    }
    return render(request, "process/edit_task.html", data)

# view result
def view_display_result(request, result_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    result = Result.objects.get(id=result_id)
    data = {
        "count": result.vehicle_count(),
        "loops": result.loop_list(),
        "result": result
    }
    return render(request, "process/result.html", data)

def view_create_intersection(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    intersections = Intersection.objects.all()
    data = {
            "intersections" : intersections,
    }
    return render(request, "process/create_intersection.html", data)