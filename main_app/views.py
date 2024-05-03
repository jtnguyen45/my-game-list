from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserGame, Note, Photo
from .forms import NoteForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import requests, environ, uuid, boto3, os
env = environ.Env()
env.read_env()

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def all_games(request):
    games_data = get_game("Harvest Moon")
    return render(request, 'all_games.html', { 'games_data': games_data })

def search_game(request):
    games_data = get_game(request.POST.get('search-term'))
    return render(request, 'all_games.html', { 'games_data': games_data })

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

@login_required
def games_index(request):
    games = UserGame.objects.filter(user=request.user)
    return render(request, 'games/index.html', {
        'games': games
    })

@login_required
def not_started(request):
    games = UserGame.objects.filter(user=request.user)
    return render(request, 'games/not_started.html', {
        'games': games
    })

@login_required
def in_progress(request):
    games = UserGame.objects.filter(user=request.user)
    return render(request, 'games/in_progress.html', {
        'games': games
    })

@login_required
def games_detail(request, game_id):
    game = UserGame.objects.get(id=game_id)
    note_form = NoteForm()
    return render(request, 'games/detail.html', {
        'game': game,
        'note_form': note_form,
    })

@login_required
def add_note(request, game_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        game = UserGame.objects.get(id=game_id)
        new_note = form.save(commit=False)
        new_note.user_game = game
        new_note.save()
    return redirect('detail', game_id=game_id)

@login_required
def edit_note(request, game_id, note_id):
    game = UserGame.objects.get(id=game_id)
    note = Note.objects.get(id=note_id)
    form = NoteForm(request.POST, instance=note)
    if form.is_valid():
        form.save()
        return redirect('detail', game_id=game_id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'main_app/edit_note.html', {
        'form': form,
        'game': game,
    })

@login_required
def delete_note(request, game_id, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('detail', game_id=game_id)

@login_required
def add_photo(request, game_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        url = f'{os.environ["S3_BASE_URL"]}{os.environ["S3_BUCKET"]}/{key}'
        try:
            s3.upload_fileobj(photo_file, os.environ['S3_BUCKET'], key)
            Photo.objects.create(url=url, user_game_id=game_id)
        except Exception as e:
            print('Error Uploading to S3')
            print('Exception message: ', e)
    return redirect('detail', game_id=game_id)

def get_game(user_str):
    url_games = 'https://api.igdb.com/v4/games'
    url_covers = 'https://api.igdb.com/v4/covers'
    headers = {
        'Client-ID': env('IGDB_CLIENT_ID'),
        'Authorization': env('IGDB_ACCESS_TOKEN'),
    }
    game_body = f'search "{user_str}"; fields *;'
    cover_body = 'fields image_id'

    game_response = requests.post(url_games, headers=headers, data=game_body)
    if game_response.status_code == 200:
        game_data = game_response.json()
    else:
        return None

    cover_ids = []
    for game in game_data:
        game_id = game.get('cover')
        cover_ids.append(game_id)

    cover_responses = []
    for cover_id in cover_ids:
        cover_body_with_id = f'where id = {cover_id}; fields *;'
        cover_response = requests.post(url_covers, headers=headers, data=cover_body_with_id)
        if cover_response.status_code == 200:
            cover_data = cover_response.json()
            cover_responses.append(cover_data)
        else:
            cover_responses.append(None)

    game_with_covers = []
    for game, cover_response in zip(game_data, cover_responses):
        if cover_response and len(cover_response) > 0:
            game['cover_image_id'] = cover_response[0]['image_id']
        else:
            game['cover_image_id'] = None
        game_with_covers.append(game)

    return game_with_covers

class GameCreate(LoginRequiredMixin, CreateView):
    model = UserGame
    fields = ['name', 'summary', 'cover', 'rating', 'status']
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