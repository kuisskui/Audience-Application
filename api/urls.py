from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.webhook, name="webhook"),
    path("audiences/", views.audiences, name="audiences")
]
