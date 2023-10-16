from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from user_profile.models import UserProfile


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            gender = form.cleaned_data.get("gender")
            year = form.cleaned_data.get("year")
            country_id = form.cleaned_data.get("country_id")
            profile = UserProfile.objects.create(user=user, gender=gender, year=year, country_id=country_id)
            profile.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("audience:dashboard")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "registration/register.html", {"register_form": form})
