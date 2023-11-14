from django.urls import path
from . import views

app_name = "audience"
urlpatterns = [
    path('scoreboard/', views.scoreboard, name="scoreboard"),
    path('', views.homepage, name="homepage"),
    path('sport_program/', views.sport_program, name="sport_program"),
    path("sports/", views.sports, name="sports"),
    path("sport/<int:sport_id>", views.sport, name="sport"),

    # Function
    path("subscribe/<int:sport_id>", views.subscribe, name="subscribe"),
    path("unsubscribe/<int:sport_id>", views.unsubscribe, name="unsubscribe"),
]
