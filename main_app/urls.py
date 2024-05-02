from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='index'),
    path('all_games/', views.all_games, name='all_games'),
    path('games/not_started/', views.not_started, name='not_started'),
    path('games/in_progress', views.in_progress, name='in_progress'),
    path('games/<int:game_id>/', views.games_detail, name='detail'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/signup/', views.signup, name='signup'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:game_id>/add_note/', views.add_note, name='add_note'),
    path('games/<int:game_id>/edit_note/<int:note_id>', views.edit_note, name='edit_note'),
    path('games/<int:game_id>/delete_note/<int:note_id>', views.delete_note, name='delete_note'),
]