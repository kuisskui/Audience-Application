from audience.models import Sport, Score, Country, Type
from user_profile.models import UserProfile
from django.http import JsonResponse


# Create your views here.
def webhook(request):
    sport_id = request.Post.get('sport_id')
    sport_name = request.Post.get('sport_name')
    sport_type_id = request.Post.get('sport_type_id')
    sport_type = request.Post.get('sport_type')
    participant = request.Post.get('participant')
    sport = Sport.object.get(sport_id=sport_id)
    # not done


def update_audience_info(request):
    profiles = UserProfile.objects.all()
    print(profiles[1].year)
    for profile in profiles:
        print(profile.user.username, f"gender: {profile.gender}", f"year: {profile.year}", f"country_id: {profile.country_id}", f"sport_id: {profile.sport_ids.all()}")
    data = {
        "audience": [
            {
                "country": "FR",
                "sport_ids": ["01", "02", "03"],
                "gender": "M",
                "age": 30
            },
            {
                "country": "TH",
                "sport_ids": ["11", "12"],
                "gender": "F",
                "age": 24
            },
        ]
    }
    return JsonResponse(data)
