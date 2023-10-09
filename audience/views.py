from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def dashboard(request):
    context = {"page": "dashboard"}
    return render(request, "audience/dashboard.html", context)

