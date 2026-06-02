from django.shortcuts import render, get_object_or_404
from .models import Game, GradedItem


def all_products(request):
    """
    Display all games
    """

    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'store/store.html', context)

def game_detail(request, game_id):
    """
    Display a single game and its graded copies
    """

    game = get_object_or_404(Game, pk=game_id)

    items = game.graded_items.all().order_by('-is_available', '-price')

    context = {
        'game': game,
        'items': items,
    }

    return render(
        request,
        'store/game_detail.html',
        context
    )