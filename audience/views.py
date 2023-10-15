from django.shortcuts import render
from django.http import JsonResponse
import requests


# Create your views here.
def dashboard(request):
    response = requests.get('http://127.0.0.1:8000/get_dashboard')
    context = {"page": "dashboard", "detail": "show total medals for every countries", "data": response.json()}
    return render(request, "audience/dashboard.html", context)


def sports(request):
    context = {"page": "sports", "detail": "show all sports without any detail or information."}
    return render(request, "audience/sports.html", context)


def sport(request, pk):
    context = {"page": "sport", "detail": f"show detail on each sport(pk ={pk})."}
    return render(request, "audience/sport.html", context)


# For testing
def get_dashboard(request):
    data = {
        "FR": {
            "gold": 100,
            "silver": 100,
            "bronze": 100
        },
        "US": {
            "gold": 100,
            "silver": 100,
            "bronze": 100
        }
    }
    print("return!!")
    return JsonResponse(data)
