from django.urls import path
from . import views

urlpatterns = [
    path("audience/<int:audience_id>", views.audience, name="audience")
]
