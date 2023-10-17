from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.webhook, name="webhook"),
    path("update_audience_info/", views.update_audience_info, name="update_audience_info")
]
