import requests
from dotenv import dotenv_values
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

config = dotenv_values(".env")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    country = models.CharField(max_length=50, null=True)
    sport_ids = models.TextField(blank=True, null=True)


@receiver(post_save, sender=UserProfile)
def update_user_profile(sender, instance, created, **kwargs):
    """Perform when a profile instance is updated or created"""
    post_url = config["POST_URL"]
    payload = {
        "id": instance.pk,
        "country": instance.country,
        "sport_ids": [] if instance.sport_ids is None else list(map(int, instance.sport_ids.split(','))),
        "gender": instance.gender,
        "age": int(instance.age)
    }
    headers = {
        "Authorization": config["AUTHORIZATION"],
        "Content-Type": "application/json"
    }
    # requests.post(url, json=payload, headers=headers)
