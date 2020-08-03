from django import forms

class SummonerForm(forms.Form):
    summonerName = forms.CharField(label="Enter Summoner Name here...", max_length=100)