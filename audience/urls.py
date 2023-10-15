from django.contrib import admin
from django.urls import path
from . import views

app_name = "audience"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path("sports/", views.sports, name="sports"),
    path("sport/<int:pk>", views.sport, name="sport"),

    # For testing get data
    path('get_dashboard/', views.get_dashboard, name="get_dashboard"),
]
