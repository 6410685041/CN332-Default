from django.shortcuts import render
from django.urls import reverse
from process.models import Task, Intersection, Loop, Result
from django.http import HttpResponseRedirect, JsonResponse
from django.utils import timezone
from celery.result import AsyncResult
from random import random
from .tasks import abc
from .models import Task

# test celery
def process_view(request):
    # Example list of task IDs you might be tracking
    tracked_tasks = Task.objects.all().order_by('created_at')  # Get all tasks, newest first
    tasks = []

    for tracked_task in tracked_tasks:
        result = AsyncResult(tracked_task.task_id)
        tasks.append({
            'id': tracked_task.task_id,
            'name': tracked_task.name,  # Assuming you want to display the name/description
            'status': result.status,
            'result': result.result if result.ready() else 'N/A',
        })
    return render(request, "process/process_view.html", {'tasks': tracked_tasks})

    
def start_task(request):
    """Initiate a task and return its ID to the frontend."""
    task = abc.delay(random(), random())
    Task.objects.create(task_id=task.id, intersection_id=1)
    
    return JsonResponse({'task_id': task.id})

def task_status(request, task_id):
    """Check the task status and return the result if completed."""
    task = abc.AsyncResult(task_id)
    if task.ready():
        return JsonResponse({'status': 'SUCCESS', 'result': task.result})
    else:
        return JsonResponse({'status': 'PENDING'})


# go to upload page (for upload video)
def view_create_task(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    intersections = Intersection.objects.all()
    data = {"intersections": intersections}
    return render(request, "process/create_task.html", data)


def view_edit_task(request, task_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    task = Task.objects.get(id=task_id)
    data = {
        "task": task,
    }
    return render(request, "process/edit_task.html", data)


# def create_task(request):
#     if request.method == "POST":
#         status = "In process"
#         time = timezone.now()
#         video = request.POST["video"]
#         intersection = request.POST["intersection"]
#         Intersection.objects.get_or_create(intersection_name=intersection)
#         task = Task.objects.create(
#             video=video, intersection=intersection, time=time, status=status
#         )
#         task.save()
#         reverse("edit_task", task.id)

def create_task(request):
    if request.method == "POST":
        status = "In process"
        time = timezone.now()
        video = request.FILES.get("video")
        intersection_name = request.POST.get("intersection")

        # Check if intersection_name is not empty
        if intersection_name:
            # Create or get the intersection instance
            intersection_instance, created = Intersection.objects.get_or_create(intersection_name=intersection_name)
            
            # Create the task with the intersection instance
            task = Task.objects.create(
                video=video, intersection=intersection_instance, created_at=time, status=status
            )
            
            # Save the task
            task.save()
            
            # Redirect to the edit page of the created task
            return HttpResponseRedirect(reverse("edit_task", args=(task.id,)))
        else:
            # Handle the case where intersection_name is empty
            # Here you can redirect to an error page or display a message
            return HttpResponseRedirect(reverse("upload_task"))  # Example redirect to an error page



# receive loop points
#       data - points
#       task_id - for specific task
def add_loop(request, data, task_id):
    if request.method == "POST":

        points = []  # encypt point from frontend

        task = Task.objects.get(id=task_id)
        name = request.POST["loop_name"]
        loop = Loop.objects.create(loop_name=name, points=points, task=task)
        loop.save()
        reverse("edit_task", task.id)


def remove_loop(request, loop_id):
    loop = Loop.objects.get(id=loop_id)
    task_id = loop.task.id
    loop.delete()
    reverse("edit_task", task_id)


def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    reverse("my_queue")

def submit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    reverse("my_queue")

def view_display_result(request, result_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    result = Result.objects.get(id=result_id)
    data = {
        "count": result.vehicle_count,
        "JSON": result.vehicle_with_direction,
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
    
def create_intersection(request):
    if request.method == "POST":
        location = request.POST["location"]
        intersection_name = request.POST["intersection_name"]
        Intersection.objects.create(
            location=location,
            intersection_name=intersection_name
        )
        return reverse("view_create_intersection")