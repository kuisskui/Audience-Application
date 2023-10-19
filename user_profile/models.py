from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    country = models.CharField(max_length=50, null=True)
    sport_ids = models.TextField(blank=True, null=True)


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         print(instance)
#         UserProfile.objects.create(user=instance)
#     instance.userprofile.save()
