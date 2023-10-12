from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def dashboard(request):
    for key, value in request.session.items():
        print(f'{key}: {value}')
    context = {"page": "dashboard", "detail": "show total medals for every countries"}
    return render(request, "audience/dashboard.html", context)


def sport(request):
    context = {"page": "sport", "detail": "show all sports without any detail or information."}
    return render(request, "audience/sport.html", context)

