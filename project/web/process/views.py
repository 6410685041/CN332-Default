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
                'direction': direction
            })
    
    # Convert parsed data to DataFrame
    df = pd.DataFrame(parsed_data)

    # Unique vehicle types and directions
    all_vehicle_types = ['car', 'truck', 'bike']
    all_directions = ['Left', 'Right', 'Entered']
    
    # Map original direction values to standard ones
    direction_map = {
        'LEFT': 'Left',
        'RIGHT': 'Right',
        'ENTERED': 'Entered'
    }
    df['direction'] = df['direction'].map(direction_map)

    # Unique loop IDs
    loop_ids = df['loop_id'].unique()
    
    summaries_by_loop_id = {}
    
    for loop_id in loop_ids:
        loop_data = df[df['loop_id'] == loop_id]
        pivot_table = loop_data.pivot_table(index='vehicle_type', columns='direction', aggfunc='size', fill_value=0)
        
        # Reindex to ensure all vehicle types and directions are included
        pivot_table = pivot_table.reindex(index=all_vehicle_types, columns=all_directions, fill_value=0)
        
        # Reset index for easier manipulation
        pivot_table = pivot_table.reset_index()
        
        # Calculate total for each vehicle type
        pivot_table['Total'] = pivot_table[['Left', 'Right', 'Entered']].sum(axis=1)
        
        # Convert to dictionary format for the template
        loop_summary_dict = pivot_table.to_dict(orient='records')
        
        # Calculate overall totals for each loop ID
        overall_totals = pivot_table[['Left', 'Right', 'Entered', 'Total']].sum().to_dict()
        overall_totals['vehicle_type'] = 'Total'
        
        loop_summary_dict.append(overall_totals)
        summaries_by_loop_id[loop_id] = loop_summary_dict
    
    data = {
        'task_id': task_id,
        'results': parsed_data,
        'summaries_by_loop_id': summaries_by_loop_id
    }
    
    return render(request, "process/result.html", data)


@login_required
def view_create_intersection(request):
    intersections = Intersection.objects.all()
    data = {
            "intersections" : intersections,
    }
    return render(request, "process/create_intersection.html", data)