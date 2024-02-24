from django.shortcuts import render
from user.models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def view_home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    profile = Profile.objects.get(id=request.user.id)
    data = {
        "profile": profile,
    }

    return render(request, "index.html", data)


def view_profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    profile = Profile.objects.get(id=request.user.id)
    data = {
        "profile": profile,
    }
    return render(request, "user/profile.html", data)


def view_edit_profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    profile = Profile.objects.get(id=request.user.id)
    data = {
        "profile": profile,
    }
    return render(request, "user/edit_profile.html", data)


def submit_edit_profile(request):
    if request.method == "POST":
        profile = Profile.objects.get(id=request.user.id)
        profile.first_name = request.POST["first_name"]
        profile.last_name = request.POST["last_name"]
        profile.email = request.POST["email"]
        profile.username = request.POST["username"]
        profile.occupation = request.POST["occupation"]
        profile.phone_number = request.POST["phone_number"]
        profile.bio = request.POST["bio"]
        profile.save()

        return reverse("profile")
