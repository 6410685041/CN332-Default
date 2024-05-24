from django.shortcuts import render
from django.urls import reverse
from process.models import Task
from django.http import HttpResponseRedirect

from celery.result import AsyncResult

# do not use @login_required decorator.
# if do, user will cannot access the occupation selection page.
# def home(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse("account_login"))
#     results = Result.objects.all()
#     return render(request, "home.html", {'results': results})

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))

    tasks = Task.objects.all()

    for task in tasks:
        task_result = AsyncResult(task.id)
        if task_result.state == 'PENDING':
            task.status = "In process"
        elif task_result.state == 'SUCCESS':
            task.status = "Success"
        elif task_result.state == 'FAILURE':
            task.status = "Fail"
        # else:
        #     task.status = task_result.state
        
        task.save()

    return render(request, "home.html", {'results': tasks})