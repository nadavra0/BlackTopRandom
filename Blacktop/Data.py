import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'Blacktop.settings')
import django
django.setup()


from players.models import Player
import requests
from bs4 import BeautifulSoup


def all_teams(main_link):
    teams=[]
    page = requests.get(main_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    rows = soup.find("table").find("tbody").find_all("tr")
    for row in rows:
        link=row.find("a")
        teams.append(link["href"])

    return teams

def player_basic(soup):
    rows=soup.find("table").find("tbody").find_all("tr")
    team=soup.find("h1",{"class": "header-title pt-2 mb-0"}).text
    for row in rows:
        try:
          cells=row.find_all("td")
          name=cells[1].find("span", {"class": "entry-font"}).text
          pos_cell=cells[1].find("span", {"class": "entry-subtext-font crop-subtext-font"})
          pos=pos_cell.find("a").text
          ovr=cells[2].text
          player=Player(team=team,name=name,pos=pos,ovr=ovr)
          print(player)
          player.save()

        except:
            pass


team_list=all_teams("https://www.2kratings.com/teams")
for team in team_list:
    print(team)
    page = requests.get(team)
    soup = BeautifulSoup(page.content, 'html.parser')
    player_basic(soup)