from django.shortcuts import render
from .models import UserGame
import requests, environ
env = environ.Env()
env.read_env()

def home(request):
    games_data = get_game() #test connection to api, TODO: remove
    return render(request, 'home.html', {'games_data': games_data})

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = UserGame.objects.all()
    return render(request, 'games/index.html', {
        'games': games
    })

def games_detail(request, game_id):
    game = UserGame.objects.get(id=game_id)
    return render(request, 'games/detail.html', {
        'game': game,
    })


def get_game():
    url = 'https://api.igdb.com/v4/games'
    headers = {
        'Client-ID': env('IGDB_CLIENT_ID'),
        'Authorization': env('IGDB_ACCESS_TOKEN'),
    }
    body = 'fields *;'
    response = requests.post(url, headers=headers, data=body)
    if response.status_code == 200:
        return response.json()
    else:
        return None