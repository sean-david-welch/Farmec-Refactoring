from django.shortcuts import render
from suppliers.views import models

def home(request):
    context = {
        'models': models
    }
    return render(request, 'home.html', context)