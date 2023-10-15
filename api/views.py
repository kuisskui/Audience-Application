from audience.models import Sport, Score, Country, Type


# Create your views here.
def webhook(request):
    sport_id = request.Post.get('sport_id')
    sport_name = request.Post.get('sport_name')
    sport_type_id = request.Post.get('sport_type_id')
    sport_type = request.Post.get('sport_type')
    participant = request.Post.get('participant')
    sport = Sport.object.get(sport_id=sport_id)