from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio

def index(request):
    return render(request, 'home.html')
