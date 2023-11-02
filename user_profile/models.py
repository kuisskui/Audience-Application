import requests
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    country = models.CharField(max_length=50, null=True)
    sport_ids = models.TextField(blank=True, null=True)


@receiver(post_save, sender=UserProfile)
def update_user_profile(sender, instance, created, **kwargs):
    """Perform when a profile instance is updated or created"""
    url = f"http://example_domain/audient/update_audient_info"
    payload = {
        "id": instance.pk,
        "country": instance.country,
        "sport_ids": None if instance.sport_ids is None else instance.sport_ids.split(','),
        "gender": instance.gender,
        "age": instance.age
    }
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }
    print(payload)
    # requests.post(url, json=payload, headers=headers)
