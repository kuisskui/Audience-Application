from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from user_profile.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            gender = form.cleaned_data.get("gender")
            age = form.cleaned_data.get("age")
            country = form.cleaned_data.get("country")
            profile = UserProfile.objects.create(user=user, gender=gender, age=age, country=country)
            profile.save()
            
            # Explicitly specify the backend when calling login
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            messages.success(request, "Registration successful.")
            return redirect("audience:dashboard")
        
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "account/register.html", {"register_form": form})

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            login(request, form.get_user())
            return redirect("audience:dashboard")  # Change this to your desired login success URL
    else:
        form = AuthenticationForm()
    
    return render(request, "account/login.html", {"form": form})

@login_required
def update_profile(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = request.user  # Use the currently authenticated user
            gender = form.cleaned_data.get("gender")
            age = form.cleaned_data.get("age")
            country = form.cleaned_data.get("country")
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.gender = gender
            profile.age = age
            profile.country = country
            profile.save()
            messages.success(request, "Profile information updated successfully.")
            return redirect("audience:dashboard")
        else:
            messages.error(request, "Unsuccessful profile update. Invalid information.")
    else:
        form = NewUserForm(instance=request.user)  # Populate the form with user data
    return render(request, "account/register.html", {"register_form": form})