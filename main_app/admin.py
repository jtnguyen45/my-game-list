from django.contrib import admin
from .models import Game, UserGame, Note, Photo

# Register your models here.
admin.site.register([Game, UserGame, Note, Photo])