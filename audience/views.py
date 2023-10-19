from django.shortcuts import render
from django.http import JsonResponse
import requests


# Create your views here.
def dashboard(request):
    response = requests.get('http://127.0.0.1:8000/get_dashboard')
    context = {"page": "dashboard", "detail": "show total medals for every countries", "data": response.json()}
    return render(request, "audience/dashboard.html", context)


def sports(request):
    response = requests.get('http://127.0.0.1:8000/get_sports')
    context = {"page": "sports", "detail": "show all sports without any detail or information.",
               "data": response.json()}
    return render(request, "audience/sports.html", context)


def sport(request, sport_id):
    response = requests.get(f'http://127.0.0.1:8000/get_sport/{sport_id}')
    context = {"page": "sport", "detail": f"show detail on each sport(sport_id ={sport_id}).", "data": response.json()}
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


def get_sports(request):
    data = {
        "01": "Atheletics",
        "02": "Archery",
        "03": "Artistic Gymnastics",
        "04": "Artistic Swimming",
    }
    return JsonResponse(data)


def get_sport(request, sport_id):
    data = {
        "sport": sport_id,
        "sport_name": "Atheletics",
        "gold": 100,
        "silver": 100,
        "bronze": 100,
        "individual_countries": [
            {
                "country_code": "FR",
                "gold": 10,
                "silver": 10,
                "bronze": 10
            },
            {
                "country_code": "US",
                "gold": 10,
                "silver": 10,
                "bronze": 10
            }
        ]
    }
    return JsonResponse(data)
