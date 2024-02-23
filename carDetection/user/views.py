from django.shortcuts import render
from user.models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return render("index.html")

def edit_profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    profile = Profile.objects.get(id=request.user)
    return render(request,'edit_profile.html',{'profile': profile})

def submit_edit(request):
    if request.method == 'POST':
        profile = Profile.objects.get(id=request.user)

        profile.first_name = request.POST['first_name']
        profile.last_name = request.POST['last_name']
        profile.email = request.POST['email']
        profile.phone_number = request.POST['phone_number']
        profile.bio = request.POST['bio']

        profile.save()
        return reverse("index.html")