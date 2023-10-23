from django.shortcuts import render, redirect
from django.http import JsonResponse
from user_profile.models import UserProfile
from django.contrib.auth.decorators import login_required
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


@login_required
def subscribe(request, sport_id):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    try:
        sport_ids = list(profile.sport_ids.split(','))
    except Exception:
        sport_ids = []
    if sport_id not in sport_ids:
        sport_ids.append(sport_id)
        profile.sport_ids = ','.join(sport_ids)
        profile.save()
    return redirect("audience:sports")


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
    return JsonResponse(data)


def get_sports(request):
    data = {
        "1": "Atheletics",
        "2": "Archery",
        "3": "Artistic Gymnastics",
        "4": "Artistic Swimming",
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
