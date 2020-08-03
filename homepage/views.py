from django.http import HttpResponseRedirect
from django.shortcuts import render

from forms import SummonerForm

# Create your views here.


def homepage_view(request, *args, **kwargs):
    return render(request, "homepage.html", {})

# TODO: Create a form to return summoner name
# def get_summonerName(request):
    
