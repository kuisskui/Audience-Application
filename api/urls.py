from django.urls import path, include
from . import views

urlpatterns = [
    path("audience/<int:audience_id>", views.audience, name="audience")
]
