from django.contrib import admin
from .models import Game, UserGame, Note

# Register your models here.
admin.site.register([Game, UserGame, Note])