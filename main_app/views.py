from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserGame
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import requests, environ
env = environ.Env()
env.read_env()

def home(request):
    games_data = get_game() #test connection to api, TODO: remove
    return render(request, 'home.html', {'games_data': games_data})

def about(request):
    return render(request, 'about.html')

@login_required
def games_index(request):
    games = UserGame.objects.filter(user=request.user)
    return render(request, 'games/index.html', {
        'games': games
    })

@login_required
def games_detail(request, game_id):
    game = UserGame.objects.get(id=game_id)
    return render(request, 'games/detail.html', {
        'game': game,
    })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def get_game():
    url = 'https://api.igdb.com/v4/games'
    headers = {
        'Client-ID': env('IGDB_CLIENT_ID'),
        'Authorization': env('IGDB_ACCESS_TOKEN'),
    }
    body = 'search "Harvest Moon"; fields *;'
    response = requests.post(url, headers=headers, data=body)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

class GameCreate(LoginRequiredMixin, CreateView):
    model = UserGame
    fields = ['name', 'cover', 'rating', 'status']
    success_url = '/games/{id}'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class GameUpdate(LoginRequiredMixin, UpdateView):
    model = UserGame
    fields = ['rating', 'status']

class GameDelete(LoginRequiredMixin, DeleteView):
    model = UserGame
    success_url = '/games'