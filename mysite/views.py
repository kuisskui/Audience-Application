from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.userprofile.gender = form.cleaned_data.get("gender")
            user.userprofile.age = form.cleaned_data.get("age")
            user.userprofile.country = form.cleaned_data.get("country")
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("audience:dashboard")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "registration/register.html", {"register_form": form})
