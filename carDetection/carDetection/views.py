from django.shortcuts import render
from django.urls import reverse
from process.models import Result
from django.http import HttpResponseRedirect

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    results = Result.objects.all()
    return render(request, "index.html", {'results': results})