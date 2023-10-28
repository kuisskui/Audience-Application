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


def sport_program(request, sport_id):
    return render(request, "audience/sport_program.html", {"sport_id": sport_id})


@login_required
def subscribe(request, sport_id):
    profile = UserProfile.objects.get(user=request.user)
    sport_ids = profile.sport_ids
    if sport_ids:
        sport_ids = f"{sport_ids},{sport_id}"
    else:
        sport_ids = sport_id
    profile.sport_ids = sport_ids
    profile.save()
    return redirect("audience:sports")


@login_required
def unsubscribe(request, sport_id):
    profile = UserProfile.objects.get(user=request.user)
    sport_ids = list(profile.sport_ids.split(','))
    if str(sport_id) in sport_ids:
        sport_ids.remove(str(sport_id))
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
