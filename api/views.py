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


def audiences(request):
    profiles = UserProfile.objects.all()
    # print(profiles[1].year)
    data = []
    for profile in profiles:
        sport_ids = list(map(int, profile.sport_ids.split(',')))
        audience = {
            "country": profile.country,
            "sport_ids": sport_ids,
            "gender": profile.gender,
            "age": int(profile.age)
        }
        data.append(audience)
        # print(profile.user.username, f"gender: {profile.gender}", f"year: {profile.year}",
        #       f"country_id: {profile.country_id}", f"sport_id: {profile.sport_ids.all()}")
    return JsonResponse({"audiences": data})
