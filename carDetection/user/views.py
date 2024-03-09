from django.shortcuts import render
from user.models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse
from process.models import Task

# Create your views here.

'''
render
'''
# view home
def view_home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    profile = Profile.objects.get(id=request.user.id)
    data = {
        "profile": profile,
    }
    return render(request, "index.html", data)

# view profile
def view_profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    profile = Profile.objects.get(id=request.user.id)
    data = {
        "profile": profile,
    }
    return render(request, "user/profile.html", data)

# view my_queue
def view_my_queue(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    profile = Profile.objects.get(id=request.user.id)
    tasks = Task.objects.all()
    data = {
        "profile": profile,
        "tasks": tasks,
    }
    return render(request, "user/my_queue.html", data)

# view edit profile
def view_edit_profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    profile = Profile.objects.get(id=request.user.id)
    data = {
        "profile": profile,
    }
    return render(request, "user/edit_profile.html", data)