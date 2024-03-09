from django.shortcuts import render
from django.urls import reverse
from process.models import Result
from django.http import HttpResponseRedirect

# do not use @login_required decorator.
# if do, user will cannot access the occupation selection page.
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))
    results = Result.objects.all()
    return render(request, "home.html", {'results': results})