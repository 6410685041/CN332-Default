from user.models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse

'''
Update
'''
# edit profile
def edit_profile(request):
    if request.method == "POST":
        profile = Profile.objects.get(id=request.user.id)
        profile.first_name = request.POST["first_name"]
        profile.last_name = request.POST["last_name"]
        profile.email = request.POST["email"]
        profile.phone_number = request.POST["phone_number"]
        profile.bio = request.POST["bio"]
        profile.save()

        return HttpResponseRedirect(reverse("profile"))