from django.shortcuts import redirect
from django.urls import reverse
from process.models import Task, Intersection, Loop
from django.http import HttpResponseRedirect, JsonResponse
from random import random
from .tasks import abc
from .models import Task
from user.models import Profile
from datetime import datetime
import pytz
import os
import json
from django.conf import settings

'''
delete
'''
# delete task
def delete_task(request, task_id):
    task = Task.objects.delete(id=task_id)
    return redirect('my_queue')

# delete result
def delete_result(request, result_id):
    Task.objects.delete(id=result_id)
    return redirect('home')

# delete intersection
def delete_intersection(request, intersection_id):
    Intersection.objects.delete(id=int(intersection_id))
    return redirect('view_create_intersection')

# delete loop
def delete_loop(request, loop_id):
    Loop.objects.delete(id=int(loop_id))
    return redirect('view_edit_task')
    
# create interaection
def create_intersection(request):
    if request.method == "POST":
        location = request.POST["location"]
        intersection_name = request.POST["intersection_name"]
        Intersection.objects.create(
            location=location,
            intersection_name=intersection_name
        )
        return redirect("view_create_intersection")
    
# in process
def create_task(request):
    if request.method == "POST":
        status = "Created"
        time = datetime.now(pytz.timezone("Asia/Bangkok"))
        owner = Profile.objects.get(id=request.user.id)
        video = request.FILES.get("video")
        intersection_id = request.POST["intersection"]
        intersection_instance = Intersection.objects.get(id=intersection_id)
        task = Task.objects.create(
            video=video, intersection=intersection_instance, created_at=time, status=status, owner=owner
        )
        task.save()
        
        # Redirect to the edit page of the created task
        return HttpResponseRedirect(reverse("view_edit_task", args=(task.id,)))
    
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

# utils
def create_summary(task_id, loop_path=None):
    task = Task.objects.get(id = task_id)
    loops = Loop.objects.filter(task = task)

    base_dir = settings.BASE_DIR

    data = []

    for i in range(len(loops)):
        lcar = 0
        ltruck = 0
        lbike = 0

        rcar = 0
        rtruck = 0
        rbike = 0

        scar = 0
        struck = 0
        sbike = 0

        if loop_path != None:
            loop_path_full = str(base_dir)+loop_path

            with open(loop_path_full, 'r') as file:
                read_data = file.read()

            read_data = read_data.split("\n")

            for j in read_data[:-1]:
                j = j.split(',')
                direction = j[-1]
                type = j[2]

                if int(j[0]) == i:
                    if direction == "LEFT":
                        if type == "car":
                            lcar += 1
                        elif type == "truck":
                            ltruck += 1
                        else:
                            lbike += 1
                    elif direction == "RIGHT":
                        if type == "car":
                            rcar += 1
                        elif type == "truck":
                            rtruck += 1
                        else:
                            rbike += 1
                    elif direction == "STRAIGHT":
                        if type == "car":
                            scar += 1
                        elif type == "truck":
                            struck += 1
                        else:
                            sbike += 1
        
        tcar = lcar+rcar+scar
        ttruck = ltruck+rtruck+struck
        tbike = lbike+rbike+sbike
        tall = tcar+ttruck+tbike
                    
        data.append({
            "name": loops[i].loop_name,
            "direction": ["", "Left", "Right", "Straight", "Total"],
            "type": [
                ["Car", lcar, rcar, scar, tcar],
                ["Truck", ltruck, rtruck, struck, ttruck],
                ["Bike", lbike, rbike, sbike, tbike],
                ["Total", lbike, rbike, sbike, tall],
            ]
        })

    sum_lcar = 0
    sum_ltruck = 0
    sum_lbike = 0

    sum_rcar = 0
    sum_rtruck = 0
    sum_rbike = 0

    sum_scar = 0
    sum_struck = 0
    sum_sbike = 0

    if loop_path != None:
        for d in data:
            sum_lcar += d['type'][0][1]
            sum_ltruck += d['type'][1][1]
            sum_lbike += d['type'][2][1]

            sum_rcar += d['type'][0][2]
            sum_rtruck += d['type'][1][2]
            sum_rbike += d['type'][2][2]

            sum_scar += d['type'][0][3]
            sum_struck += d['type'][1][3]
            sum_sbike += d['type'][2][3]

    sum_tcar = sum_lcar+sum_rcar+sum_scar
    sum_ttruck = sum_ltruck+sum_rtruck+sum_struck
    sum_tbike = sum_lbike+sum_rbike+sum_sbike
    sum_all = sum_tcar+sum_ttruck+sum_tbike
    summary = [{
        "type": [
            ["Car", sum_lcar, sum_rcar, sum_scar, sum_tcar],
            ["Truck", sum_ltruck, sum_rtruck, sum_struck, sum_ttruck],
            ["Bike", sum_lbike, sum_rbike, sum_sbike, sum_tbike],
            ["Total", sum_lbike, sum_rbike, sum_sbike, sum_all],
        ]}
    ]
    data = {
        "loops":data,
        "summary":summary
    }
    
    directory = str(base_dir)+"\\media/summary/"
    file_path = os.path.join(directory, f"data{task_id}.json")
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist
 
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f"JSON file {task_id} created successfully.")
    except IOError:
        print("An error occurred while creating the JSON file.")

    return file_path