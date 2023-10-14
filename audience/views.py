from django.shortcuts import render


# Create your views here.
def dashboard(request):
    context = {"page": "dashboard", "detail": "show total medals for every countries"}
    return render(request, "audience/dashboard.html", context)


def sports(request):
    context = {"page": "sports", "detail": "show all sports without any detail or information."}
    return render(request, "audience/sports.html", context)


def sport(request, pk):
    context = {"page": "sport", "detail": f"show detail on each sport(pk ={pk})."}
    return render(request, "audience/sport.html", context)
