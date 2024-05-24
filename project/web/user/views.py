from django.shortcuts import render, redirect
from user.models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse
from process.models import Task
from .forms import OccupationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

"""
render
"""


# view home
@login_required
def view_home(request):
    profile = Profile.objects.get(id=request.user.id)
    data = {
        "profile": profile,
    }
    return render(request, "index.html", data)


# view profile
@login_required
def view_profile(request):
    profile = Profile.objects.get(id=request.user.id)
    data = {
        "profile": profile,
    }
    return render(request, "user/profile.html", data)


# view my_queue
@login_required
def view_my_queue(request):
    profile = Profile.objects.get(id=request.user.id)
    tasks = Task.objects.filter(owner=request.user)
    data = {
        "profile": profile,
        "tasks": tasks,
    }
    return render(request, "user/my_queue.html", data)


# view edit profile
@login_required
def view_edit_profile(request):
    profile = Profile.objects.get(id=request.user.id)
    data = {
        "profile": profile,
    }
    return render(request, "user/edit_profile.html", data)

@login_required
def view_occupation_selection(request):
     # Check if the user already has an occupation set
    if request.user.occupation:
        # Redirect to profile page
        return redirect('home')

    # Continue with the existing logic if no occupation is set
    if request.method == 'POST':
        form = OccupationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page
    else:
        form = OccupationForm(instance=request.user)

    return render(request, 'user/occupation_selection.html', {'form': form})
