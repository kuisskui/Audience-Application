from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile


# Create your views here.
@login_required
def profile(request):
    userprofile = UserProfile.objects.get(user=request.user)
    sport_ids = userprofile.sport_ids
    sport_ids = [] if sport_ids is None else sport_ids.split(',')
    print(sport_ids)
    context = {"page": "profile", "detail": "show user profile", "userprofile": userprofile, "sport_ids": sport_ids}
    return render(request, "user_profile/profile.html", context)
