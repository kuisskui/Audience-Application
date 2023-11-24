from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
import requests


# Create your views here.
@login_required
def profile(request):
    api_key = '02e2cdc6ac5d17a2bb67824c91f51ac55ce46465133f92233e3daa552120bcb3'
    sport_url = 'https://referite-6538ffaf77b0.herokuapp.com/api/schedule/sport'
    headers = {'Accept': 'application/json', 'Authorization': api_key}

    try:
        data = requests.get(sport_url, headers=headers).json()
        userprofile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If the user profile does not exist, redirect to complete-registration
        return redirect('update_profile')

    sport_ids = userprofile.sport_ids
    sport_ids = [] if sport_ids is None else sport_ids.split(',')
    sport_ids.sort()
    context = {"page": "profile", "detail": "show user profile", "userprofile": userprofile, "sport_ids": sport_ids,
               "sports": data}
    return render(request, "user_profile/profile.html", context)