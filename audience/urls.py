from django.contrib import admin
from django.urls import path
from . import views

app_name = "audience"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('sport', views.sport, name="sport")
]
