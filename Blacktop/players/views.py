import random

from django.shortcuts import render

# Create your views here.
import random
from django.shortcuts import render
from .models import Player

def main(req):
    all_players=list(Player.objects.all())
    team1=random.sample(all_players,5)
    team2=random.sample(all_players,5)
    dup=any(x in team1 for x in team2)
    while dup==True:
        team2 = random.sample(all_players, 5)
        dup = any(x in team1 for x in team2)

    dict={}
    dict["team1"]=team1
    dict["team2"]=team2
    return render(req, 'players/index.html', context=dict)
