from django.shortcuts import render
from .models import UserProfile


# Create your views here.
def profile(request):
    userprofile = UserProfile.objects.get(user=request.user)
    context = {"page": "profile", "detail": "show user profile", "userprofile": userprofile}
    return render(request, "user_profile/profile.html", context)
