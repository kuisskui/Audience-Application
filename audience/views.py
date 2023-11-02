import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from user_profile.models import UserProfile


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
        "5": "BasketBall"
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


def sport_program(request):
    data = {
        "schedule_list": [
            {
                "datetime": "2021-10-1T00:00:00",
                "sport": [
                    {
                        "_id": 1,
                        "revision_id": 11,
                        "sport_id": 2,
                        "sport_name": "Archery",
                        "sport_type": [
                            {
                                "_id": 2,
                                "revision_id": 22,
                                "type_id": 1,
                                "type_name": "Individual",
                                "status": "RECORDED"
                            },
                            {
                                "_id": 3,
                                "revision_id": 33,
                                "type_id": 2,
                                "type_name": "Team",
                                "status": "RECORDED"
                            }
                        ],
                        "is_ceremonies": False,
                        "sport_status": "RECORDED"
                    },
                    {
                        "_id": 1,
                        "revision_id": 11,
                        "sport_id": 2,
                        "sport_name": "BasketBall",
                        "sport_type": [
                            {
                                "_id": 2,
                                "revision_id": 22,
                                "type_id": 1,
                                "type_name": "Individual",
                                "status": "RECORDED"
                            },
                            {
                                "_id": 3,
                                "revision_id": 33,
                                "type_id": 2,
                                "type_name": "Team",
                                "status": "RECORDED"
                            }
                        ],
                        "is_ceremonies": False,
                        "sport_status": "RECORDED"
                    }
                ]
            },
            {
                "datetime": "2021-10-2T00:00:00",
                "sport": [
                    {
                        "_id": 1,
                        "revision_id": 11,
                        "sport_id": 2,
                        "sport_name": "Batminton",
                        "sport_type": [
                            {
                                "_id": 2,
                                "revision_id": 22,
                                "type_id": 1,
                                "type_name": "Individual",
                                "status": "RECORDED"
                            },
                            {
                                "_id": 3,
                                "revision_id": 33,
                                "type_id": 2,
                                "type_name": "Team",
                                "status": "RECORDED"
                            }
                        ],
                        "is_ceremonies": False,
                        "sport_status": "RECORDED"
                    }
                ]
            },
            {
                "datetime": "2021-10-3T00:00:00",
                "sport": [
                    {
                        "_id": 1,
                        "revision_id": 11,
                        "sport_id": 2,
                        "sport_name": "BasketBall",
                        "sport_type": [
                            {
                                "_id": 2,
                                "revision_id": 22,
                                "type_id": 1,
                                "type_name": "Individual",
                                "status": "RECORDED"
                            },
                            {
                                "_id": 3,
                                "revision_id": 33,
                                "type_id": 2,
                                "type_name": "Team",
                                "status": "RECORDED"
                            }
                        ],
                        "is_ceremonies": False,
                        "sport_status": "RECORDED"
                    }
                ]
            },
        ]
    }
    all_sports = {
        "1": "Atheletics",
        "2": "Archery",
        "3": "Artistic Gymnastics",
        "4": "Artistic Swimming",
        "5": "BasketBall"
    }
    context = {"data": data,
               "all_sports": all_sports}

    return render(request, "audience/sport_program.html", context)


def get_sport_program(request):
    data = {
        "schedule_list": [
            {
                "datetime": "2021-08-01T00:00:00",
                "sport": [{
                    "sport_id": 1,
                    "sport_name": "Football",
                    "sport_type": [
                        {
                            "type_id": 1,
                            "type_name": "11v11",
                            "status": "RECORDED"
                        },
                        {
                            "type_id": 2,
                            "type_name": "7v7",
                            "status": "TROPHY"
                        }
                    ],
                    "sport_status": (
                        "TROPHY"
                    )
                }

                ],

            },
            {
                "datetime": "2021-08-02T00:00:00",
                "sport": [{
                    "sport_id": 3,
                    "sport_name": "League of Legends",
                    "sport_type": [
                        {
                            "type_id": 3,
                            "type_name": "5v5",
                            "status": "RECORDED"
                        },
                        {
                            "type_id": 4,
                            "type_name": "Free For All",
                            "status": "TROPHY"
                        }
                    ],
                    "sport_status": (
                        "TROPHY"
                    )
                },
                    {
                        "sport_id": 4,
                        "sport_name": "Rocket League",
                        "sport_type": [
                        ],
                        "sport_status": (
                            "TROPHY"
                        )
                    }
                ],

            },
        ]
    }
    context = {"data": data}
    return render(request, "audience/sport_program.html", context)
