from django.shortcuts import render

# Create your views here.


def summoner_view(request, *args, **kwargs):
    return render(request, "summoner_profile.html", {})
