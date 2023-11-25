from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_profile.models import UserProfile
from requests.auth import HTTPBasicAuth
import requests
import logging
from django.http import HttpResponse


def get_datetime(data):
    return data.get('datetime')


# Create your views here.
def homepage(request):
    if not request.user.is_anonymous:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            sport_ids = list(map(int, user_profile.sport_ids.split(",")))
        except Exception:
            sport_ids = []
        header = {
            "Accept": "application/json",
            "Authorization": "02e2cdc6ac5d17a2bb67824c91f51ac55ce46465133f92233e3daa552120bcb3"
        }
        url = "https://referite-6538ffaf77b0.herokuapp.com/api/schedule/all"
        data = requests.get(url, headers=header).json()
        data["schedule_list"].sort(key=get_datetime)
        url = "https://referite-6538ffaf77b0.herokuapp.com/api/schedule/sport"
        all_sports = requests.get(url, headers=header).json()
        context = {"sport_ids": sport_ids, "all_sports": all_sports, "data": data}

        return render(request, "audience/homepage.html", context)
    return render(request, "audience/homepage.html")


def scoreboard(request):
    str_data = requests.get("https://sota-backend.fly.dev/medals/")
    data = str_data.json()
    # sorted_data = sorted(data.items(), key=lambda x: (sum(x[1].values()), x[1]['bronze'], x[1]['silver'], x[1]['gold'], x[0]))
    sorted_data = sorted(data.items(), key=lambda x: (-(x[1]['gold'] + x[1]['silver'] + x[1]['bronze']), -x[1]['gold'], -x[1]['silver'], -x[1]['bronze'], x[0]))
    context = {"page": "scoreboard", "detail": "show total medals for every countries", "data": dict(sorted_data)}
    return render(request, "audience/scoreboard.html", context)


def sports(request):
    api_key = '02e2cdc6ac5d17a2bb67824c91f51ac55ce46465133f92233e3daa552120bcb3'
    sport_url = 'https://referite-6538ffaf77b0.herokuapp.com/api/schedule/sport'
    headers = {'Accept': 'application/json', 'Authorization': api_key}

    try:
        data = requests.get(sport_url, headers=headers).json()

        # Pass user_profile to the template
        user_profile = None
        if request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=request.user)
            if user_profile.sport_ids != None:
                sport_list = [int(number) for number in user_profile.sport_ids.split(',')]
            else:
                sport_list = user_profile.sport_ids
        else:
            sport_list = None

        context = {"page": "sports", "detail": "show all sports without any detail or information.",
                   "data": data, "user_profile": user_profile, "sport_list": sport_list}
        return render(request, "audience/sports.html", context)
    
    except UserProfile.DoesNotExist:
        return redirect('update_profile') 

    except requests.RequestException as e:
        # Log the exception for debugging
        logging.error(f"Error fetching data from API: {e}")

        # Return an error response or handle the exception as needed
        return HttpResponse("Error fetching data from API", status=500)


def sport(request, sport_id):
    detail_url = f'https://sota-backend.fly.dev/medal/s/{sport_id}'

    try:
        data = requests.get(detail_url).json()
        context = {"page": "sport_detail", "detail": f"Show detail for sport ID {sport_id}", "data": data}
        return render(request, "audience/sport.html", context)

    except requests.RequestException as e:
        # Log the exception for debugging
        logging.error(f"Error fetching data from API: {e}")

        # Return an error response or handle the exception as needed
        return HttpResponse("Error fetching data from API", status=500)


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
    headers = {'Accept': 'application/json',
               'Authorization': api_key}

    try:
        data = requests.get(all_url, headers=headers).json()
        all_sports = requests.get(sport_url, headers=headers).json()

        data["schedule_list"].sort(key=get_datetime)

        context = {"data": data, "all_sports": all_sports}
        return render(request, "audience/sport_program.html", context)

    except requests.RequestException as e:
        # Log the exception for debugging
        logging.error(f"Error fetching data from API: {e}")

        # Return an error response or handle the exception as needed
        return HttpResponse("Error fetching data from API", status=500)
