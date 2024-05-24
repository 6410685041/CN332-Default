from django.shortcuts import render
from django.urls import reverse
from process.models import Result, Task
from django.http import HttpResponseRedirect

# do not use @login_required decorator.
# if do, user will cannot access the occupation selection page.
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    results = Task.objects.filter(status="Success")
    return render(request, "home.html", {'results': results})