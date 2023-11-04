from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile


# Create your views here.
@login_required
def profile(request):
    try:
        userprofile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If the user profile does not exist, redirect to complete-registration
        return redirect('update_profile')

    sport_ids = userprofile.sport_ids
    sport_ids = [] if sport_ids is None else sport_ids.split(',')
    context = {"page": "profile", "detail": "show user profile", "userprofile": userprofile, "sport_ids": sport_ids}
    return render(request, "user_profile/profile.html", context)