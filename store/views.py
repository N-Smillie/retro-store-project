from django.shortcuts import redirect, render, get_object_or_404
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

def add_to_basket(request, item_id):
    basket = request.session.get('basket', [])

    if item_id not in basket:
        basket.append(item_id)

    request.session['basket'] = basket

    return redirect('basket_view')

def view_basket(request):
    basket = request.session.get('basket', [])

    items = GradedItem.objects.filter(id__in=basket)

    context = {
        'items': items
    }

    return render(request, 'store/basket.html', context)