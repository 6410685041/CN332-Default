from django.shortcuts import render
from django.urls import reverse
from process.models import Task, Intersection, Result,Loop
from django.http import HttpResponseRedirect
from celery.result import AsyncResult
from process import functions
import json
from django.contrib.auth.decorators import login_required
import pandas as pd
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

@login_required
def count_vehicle_enter_per_loop(data):
    enter_count = {}
    for item in data:
        loop_id = item['loop_id']
        direction = item['direction']
        if direction == 'ENTERED':
            enter_count[loop_id] = enter_count.get(loop_id, 0) + 1
    return enter_count

# view result
@login_required
def view_display_result(request, task_id):
    result_path = f"static/result/{task_id}/{task_id}.txt"
    
    # Function to find direction
    def find_direction(previous, current):
        if previous['vehicle_id'] == current['vehicle_id']:
            return current['direction']
        else:
            return "STRIGHT"

    # Read and parse the file
    parsed_data = []
    with open(result_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 5:
                loop_id, vehicle_id, vehicle_type, time, direction = parts
                parsed_data.append({
                    'loop_id': int(loop_id),
                    'vehicle_id': int(vehicle_id),
                    'vehicle_type': vehicle_type,
                    'time': float(time),
                    'direction': direction.strip().upper()
                })

    # Create DataFrame and sort by vehicle_id and time
    df = pd.DataFrame(parsed_data).sort_values(by=['loop_id', 'vehicle_id', 'time'])

    print(df)
    # Initialize dictionaries
    results = {}

    skip = 0

    # Process the DataFrame
    previous = None
    for i, current in df.iterrows():
        # print(current)
        if previous is None:
            previous = current
            continue
        loop_id = previous['loop_id']
        if skip > 0:
            previous = current
            skip-=1
            if i+1 == len(df):
                if vehicle_type == 'car':
                    results[loop_id]['car']['stright'] += 1
                elif vehicle_type == 'truck':
                    results[loop_id]['truck']['stright'] += 1
                elif vehicle_type == 'bike':
                    results[loop_id]['bike']['stright'] += 1
            continue
        if loop_id not in results:
            results[loop_id] = {
                'car': {'left': 0, 'right': 0, 'stright': 0, 'total': 0},
                'truck': {'left': 0, 'right': 0, 'stright': 0, 'total': 0},
                'bike': {'left': 0, 'right': 0, 'stright': 0, 'total': 0},
            }

        direction = find_direction(previous, current)
        vehicle_type = previous['vehicle_type'].lower()

        if vehicle_type == 'car':
            if direction == 'LEFT':
                results[loop_id]['car']['left'] += 1
                skip = 1
            elif direction == 'RIGHT':
                results[loop_id]['car']['right'] += 1
                skip = 1
            elif direction == 'STRIGHT':
                results[loop_id]['car']['stright'] += 1

        elif vehicle_type == 'truck':
            if direction == 'LEFT':
                results[loop_id]['truck']['left'] += 1
                skip = 1
            elif direction == 'RIGHT':
                results[loop_id]['truck']['right'] += 1
                skip = 1
            elif direction == 'STRIGHT':
                results[loop_id]['truck']['stright'] += 1

        elif vehicle_type == 'bike':
            if direction == 'LEFT':
                results[loop_id]['bike']['left'] += 1
                skip = 1
            elif direction == 'RIGHT':
                results[loop_id]['bike']['right'] += 1
                skip = 1
            elif direction == 'STRIGHT':
                results[loop_id]['bike']['stright'] += 1

        previous = current

    # Adjust STRIGHT counts by dividing by 2 and calculate totals
    for loop_id, data in results.items():
        for vehicle_type, counts in data.items():
            counts['total'] = counts['left'] + counts['right'] + counts['stright']
    
    # Combine results into a dictionary
    data = {
        'task': Task.objects.get(id=task_id),
        'results': results,
        'parsed_data': parsed_data,
    }
    
    return render(request, "process/result.html", data)



@login_required
def view_create_intersection(request):
    intersections = Intersection.objects.all()
    data = {
            "intersections" : intersections,
    }
    return render(request, "process/create_intersection.html", data)