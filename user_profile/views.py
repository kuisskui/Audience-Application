from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile


# Create your views here.
@login_required
def profile(request):
    userprofile = UserProfile.objects.get(user=request.user)
    context = {"page": "profile", "detail": "show user profile", "userprofile": userprofile}
    return render(request, "user_profile/profile.html", context)
