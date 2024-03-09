from django.shortcuts import render
from django.urls import reverse
from process.models import Result
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    results = Result.objects.all()
    return render(request, "home.html", {'results': results})