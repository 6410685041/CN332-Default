import os
import sys
# Assuming 'detect_and_track_ooad' module is one directory above the current directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from django.shortcuts import redirect, render
from django.urls import reverse
from process.models import Task, Intersection, Loop
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from random import random
from .models import Task
from user.models import Profile
from datetime import datetime
import pytz
import os
import json
from django.conf import settings
from tasks import celery_start_task

# celery
from .tasks import add
from celery.result import AsyncResult

'''
delete
'''
# delete task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id).delete()
    return redirect('my_queue')

# delete result
def delete_result(request, result_id):
    Task.objects.get(id=result_id).delete()
    return redirect('home')

# delete intersection
def delete_intersection(request, intersection_id):
    Intersection.objects.get(id=intersection_id).delete()
    return redirect('view_create_intersection')

# delete loop
def delete_loop(request, loop_id):
    task_id = request.GET['task_id']
    Loop.objects.get(id=loop_id).delete()

    file_path = f'static/json/loop_data/{task_id}.json'

    # Load existing data from the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Find the loop data to remove
    loop_data = next((item for item in data["loops"] if item["id"] == str(loop_id)), None)
    
    if loop_data:
        # Remove the loop data from the list
        data["loops"].remove(loop_data)
    
        # Write the updated data back to the JSON file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    return HttpResponseRedirect(reverse("view_edit_task", args=(task_id,)))



    
'''
create
'''
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
test celery
'''
def add_number(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        result = celery_start_task.delay(num1, num2)
        return redirect(reverse('get_result', kwargs={'task_id': result.task_id}))
    return render(request, 'process/process_view.html')

def get_result(request, task_id):
    task = AsyncResult(task_id)
    if task.ready():
        result = task.get()
        return HttpResponse(f'The result of the addition is: {result}')
    else:
        return HttpResponse('Task is still processing. Please refresh the page.')     
        
# in process
def add_loop(request,task_id):
    if request.method == "POST":
        loop_name = request.POST.get("loop_name", "")
        orientation = request.POST.get("orientation", "")
        points = []
        # Extract x and y coordinates from request.POST and add them to the points list
        points.append({"x": request.POST["x1"], "y": request.POST["y1"]})
        points.append({"x": request.POST["x2"], "y": request.POST["y2"]})
        points.append({"x": request.POST["x3"], "y": request.POST["y3"]})
        points.append({"x": request.POST["x4"], "y": request.POST["y4"]})

        summary_location = {
                "x": int(request.POST.get("summary_location_x", "")),
                "y": int(request.POST.get("summary_location_y", ""))
            }

        # Convert the points list to JSON format
        points_json = json.dumps(points)
        summary_location_json = json.dumps(summary_location)

        task = Task.objects.get(id=task_id)
        loop = Loop.objects.create( points=points_json, task_id=task_id)
       

        request.session['loop_id'] = loop.id
        
        new_loop_data = {
               "name": loop_name,
                "id": str(loop.id),
                "points": points,
                "orientation": orientation,
                "summary_location": summary_location
                
            }
        
        file_path = f'static/json/loop_data/{task_id}.json'

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
                data = {"loops": []}
        # Append the new loop data to the list of loops
        data["loops"].append(new_loop_data)

        # Write the updated data back to the JSON file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)


        return HttpResponseRedirect(reverse("view_edit_task", args=(task.id,)))

    


# submit task and call celery_start_task
def submit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    celery_start_task.delay('../static/video/' + task.video.url, task_id)
    return HttpResponseRedirect(reverse('home'))

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