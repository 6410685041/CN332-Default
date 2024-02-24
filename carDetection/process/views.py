from django.shortcuts import render
from django.urls import reverse
from process.models import Task, Intersection, Loop
from django.http import HttpResponseRedirect
from django.utils import timezone
# Create your views here.

# go to upload page (for upload video)
def view_upload_task(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'upload_task.html')

def view_edit_task(request, task_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    task = Task.objects.get(id=task_id)
    data = {"task": task,}
    return render(request, 'edit_task.html', data)

def create_task(request):
    if request.method == 'POST':
        status = 'In process'
        time = timezone.now()
        video = request.POST['video']
        intersection = request.POST['intersection']
        Intersection.objects.get_or_create(intersection_name=intersection)
        task = Task.objects.create(video=video, intersection=intersection, time=time, status=status)
        task.save()
        reverse("edit_task" , task.id)

# receive loop points 
#       data - points
#       task_id - for specific task
def add_loop(request, data, task_id):
    if request.method == 'POST':
        
        points=[] # encypt point from frontend

        task = Task.objects.get(id=task_id)
        name = request.POST['loop_name']
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
        