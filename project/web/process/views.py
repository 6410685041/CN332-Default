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
    
    with open(result_path, 'r') as file:
        lines = file.readlines()
        
    parsed_data = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 5:
            loop_id, vehicle_id, vehicle_type, time, direction = parts
            parsed_data.append({
                'loop_id': int(loop_id),
                'vehicle_id': int(vehicle_id),
                'vehicle_type': vehicle_type,
                'time': float(time),
                'direction': direction.strip()
            })
    
    # Filter out 'ENTERED' actions
    df = pd.DataFrame(parsed_data)
    df_filtered = df[df['direction'] != 'ENTERED']
    
    # Group by Loop ID and Vehicle Type, and count the directions
    summary = df_filtered.groupby(['loop_id', 'vehicle_type', 'direction']).size().unstack(fill_value=0)
    
    # Calculate the Total column
    summary['Total'] = summary.sum(axis=1)
    
    # Reset the index for easier handling
    summary = summary.reset_index()
    
    # Prepare the summary dictionary for template rendering
    summaries_by_loop_id = {}
    for _, row in summary.iterrows():
        loop_id = row['loop_id']
        vehicle_type = row['vehicle_type']
        summary_entry = {
            'vehicle_type': vehicle_type,
            'Left': row.get('LEFT', 0),
            'Right': row.get('RIGHT', 0),
            'Straight': row.get('STRAIGHT', 0),
            'Total': row['Total']
        }
        if loop_id not in summaries_by_loop_id:
            summaries_by_loop_id[loop_id] = []
        summaries_by_loop_id[loop_id].append(summary_entry)
    
    data = {
        'task_id': task_id,
        'summaries_by_loop_id': summaries_by_loop_id,
    }
    
    return render(request, "process/result.html", data)



@login_required
def view_create_intersection(request):
    intersections = Intersection.objects.all()
    data = {
            "intersections" : intersections,
    }
    return render(request, "process/create_intersection.html", data)