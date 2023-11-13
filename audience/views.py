from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_profile.models import UserProfile
from requests.auth import HTTPBasicAuth
import requests
import logging
from django.http import HttpResponse


# Create your views here.
def dashboard(request):
    data = {
        "FR": {
            "gold": 90,
            "silver": 90,
            "bronze": 100
        },
        "US": {
            "gold": 100,
            "silver": 100,
            "bronze": 100
        },
    }
    # data = request.get("https://sota-backend.fly.dev/medals/")
    sorted_data = sorted(data.items(), key=lambda x: x[1]['gold'] + x[1]['silver'] + x[1]['bronze'], reverse=True)
    context = {"page": "dashboard", "detail": "show total medals for every countries", "data": dict(sorted_data)}
    return render(request, "audience/dashboard.html", context)


def sports(request):
    data = {
        "1": "Athletics",
        "2": "Archery",
        "3": "Artistic Gymnastics",
        "4": "Artistic Swimming",
        "5": "BasketBall"
    }
    # data = request.get("https://sota-backend.fly.dev/sports/")
    context = {"page": "sports", "detail": "show all sports without any detail or information.",
               "data": data}
    return render(request, "audience/sports.html", context)


def sport(request, sport_id):
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
    # data = request.get("https://sota-backend.fly.dev/medal/s/:sport_id")
    context = {"page": "sport", "detail": f"show detail on each sport(sport_id ={sport_id}).", "data": data}
    return render(request, "audience/sport.html", context)


@login_required
def subscribe(request, sport_id):
    sport_id = str(sport_id)
    user = request.user
    profile = UserProfile.objects.get(user=user)
    try:
        sport_ids = profile.sport_ids.split(",")
    except Exception:
        sport_ids = []
    if sport_id not in sport_ids:
        sport_ids.append(sport_id)
        result = ','.join(sport_ids)
        profile.sport_ids = result
        profile.save()
    return redirect("audience:sports")


@login_required
def unsubscribe(request, sport_id):
    profile = UserProfile.objects.get(user=request.user)
    sport_ids = list(profile.sport_ids.split(','))
    sport_ids.remove(str(sport_id))
    if not sport_ids:
        sport_ids = None
        profile.sport_ids = sport_ids
    else:
        profile.sport_ids = ','.join(sport_ids)
    profile.save()
    return redirect("user_profile:profile")


def sport_program(request):
    api_key = '02e2cdc6ac5d17a2bb67824c91f51ac55ce46465133f92233e3daa552120bcb3'
    all_url = 'https://referite-6538ffaf77b0.herokuapp.com/api/schedule/all'
    sport_url = 'https://referite-6538ffaf77b0.herokuapp.com/api/schedule/sport'
    headers = {'Accept': 'application/json'}

    auth = HTTPBasicAuth('authorization', api_key)


    try:
        data = requests.get(all_url, headers=headers, auth=auth).json()
        all_sports = requests.get(sport_url, headers=headers, auth=auth).json()

        context = {"data": data, "all_sports": all_sports}
        return render(request, "audience/sport_program.html", context)

    except requests.RequestException as e:
        # Log the exception for debugging
        logging.error(f"Error fetching data from API: {e}")

        # Return an error response or handle the exception as needed
        return HttpResponse("Error fetching data from API", status=500)
