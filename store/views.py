from django.shortcuts import redirect, render, get_object_or_404
from .models import Game, GradedItem
from django.contrib import messages
from django.views.decorators.http import require_POST

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

@require_POST
def add_to_basket(request, item_id):

    item = get_object_or_404(
        GradedItem,
        pk=item_id
    )

    basket = request.session.get('basket', [])

    if item_id not in basket:

        basket.append(item_id)

        request.session['last_added_item'] = {
            'title': item.game.title,
            'grade': item.grade,
            'price': str(item.price),
            'image': (
                item.slab_image.url
                if item.slab_image
                else ''
            ),
        }

        messages.success(
            request,
            f'{item.game.title} ({item.grade}) added to basket.'
        )

    else:

        messages.warning(
            request,
            'This item is already in your basket.'
        )

    request.session['basket'] = basket

    return redirect(
        'game_detail',
        game_id=item.game.id
    )

def view_basket(request):
    basket = request.session.get('basket', [])

    items = GradedItem.objects.filter(id__in=basket)

    context = {
        'items': items
    }

    return render(request, 'store/basket.html', context)