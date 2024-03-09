from django.shortcuts import render, redirect
from django.urls import reverse
from process.models import Task, Intersection, Loop, Result
from django.http import HttpResponseRedirect, JsonResponse
from random import random
from .tasks import abc
from .models import Task
from user.models import Profile
from datetime import datetime
import pytz

'''
delete
'''

# delete task
def delete_task(request, task_id):
    task = Task.objects.delete(id=task_id)
    return redirect('my_queue')

# delete result
def delete_result(request, result_id):
    task = Task.objects.delete(id=result_id)
    return redirect('home')

# delete intersection
def delete_intersection(request, intersection_id):
    intersection = Intersection.objects.get(id=int(intersection_id))
    intersection.delete()
    return redirect('create_intersection')

# def remove_loop(request, loop_id):
#     loop = Loop.objects.get(id=loop_id)
#     task_id = loop.task.id
#     loop.delete()
#     return reverse("edit_task", task_id)
    
def create_intersection(request):
    if request.method == "POST":
        location = request.POST["location"]
        intersection_name = request.POST["intersection_name"]
        Intersection.objects.create(
            location=location,
            intersection_name=intersection_name
        )
        return redirect("create_intersection")
    
'''
test
'''
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
    
# in process
def create_task(request):
    if request.method == "POST":
        status = "Created"
        time = datetime.now(pytz.timezone("Asia/Bangkok"))
        owner = Profile.objects.get(id=request.user.id)
        video = request.FILES.get("video")
        intersection_name = request.POST["intersection"]

        # Check if intersection_name is not empty
        if intersection_name:
            # Create or get the intersection instance
            intersection_instance, created = Intersection.objects.get_or_create(intersection_name=intersection_name)
            
            # Create the task with the intersection instance
            task = Task.objects.create(
                video=video, intersection=intersection_instance, created_at=time, status=status, owner=owner
            )
            
            # Save the task
            task.save()
            
            # Redirect to the edit page of the created task
            return HttpResponseRedirect(reverse("view_edit_task", args=(task.id,)))
        else:
            # Handle the case where intersection_name is empty
            # Here you can redirect to an error page or display a message
            return HttpResponseRedirect(reverse("upload_task"))  # Example redirect to an error page
        
# in process
def add_loop(request, data, task_id):
    if request.method == "POST":

        points = []  # encypt point from frontend

        task = Task.objects.get(id=task_id)
        name = request.POST["loop_name"]
        loop = Loop.objects.create(loop_name=name, points=points, task=task)
        loop.save()
        reverse("edit_task", task.id)
    
# in process
def submit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return reverse("my_queue")