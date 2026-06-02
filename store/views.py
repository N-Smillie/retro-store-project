from django.shortcuts import render
from .models import Game


def all_products(request):
    """
    Display all games
    """

    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'store/store.html', context)