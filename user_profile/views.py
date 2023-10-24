from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile


# Create your views here.
@login_required
def profile(request):
    userprofile = UserProfile.objects.get(user=request.user)
    sport_ids = list(userprofile.sport_ids.split(','))
    sport_ids = [] if '' in sport_ids else sport_ids
    context = {"page": "profile", "detail": "show user profile", "userprofile": userprofile, "sport_ids": sport_ids}
    return render(request, "user_profile/profile.html", context)
