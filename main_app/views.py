from django.shortcuts import render
#from .models import Game

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')