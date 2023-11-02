from django.http import JsonResponse
from user_profile.models import UserProfile


# Create your views here.
def audience(audience_id):
    profile = UserProfile.objects.get(pk=audience_id)
    sport_ids = list(map(int, profile.sport_ids.split(',')))
    data = {
        "id": profile.pk,
        "country": profile.country,
        "sport_ids": sport_ids,
        "gender": profile.gender,
        "age": int(profile.age)
    }
    return JsonResponse(data)
