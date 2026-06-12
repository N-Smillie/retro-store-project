from django.shortcuts import redirect, render, get_object_or_404
from .models import Game, GradedItem
from django.contrib import messages
from django.views.decorators.http import require_POST

def all_products(request):
    """
    Display all games with filtering.
    """

    games = Game.objects.all()

    genre = request.GET.get('genre')
    console = request.GET.get('console')
    available = request.GET.get('available')
    query = request.GET.get('q')

    # Search by title
    if query:
        games = games.filter(
            title__icontains=query
        )

    if genre:
        games = games.filter(
            genre=genre
        )

    if console:
        games = games.filter(
            console=console
        )

    # Filter games that have at least one available copy
    if available:
        games = games.filter(
            graded_items__is_available=True
        ).distinct()

    context = {
        'games': games,

        'genres': Game.GENRE_CHOICES,
        'consoles': Game.CONSOLE_CHOICES,

        'current_genre': genre,
        'current_console': console,
        'current_available': available,
        'current_query': query,
    }

    return render(
        request,
        'store/store.html',
        context
    )

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

    item_id = int(item_id)
    item = get_object_or_404(GradedItem, pk=item_id)

    if not item.is_available:

        messages.error(
            request,
            "This item has already been sold."
        )

        return redirect(
            'game_detail',
            game_id=item.game.id
        )

    basket = [int(x) for x in request.session.get('basket', [])]

    if item_id not in basket:

        basket.append(item_id)

        request.session['toast_item'] = {
            'title': item.game.title,
            'grade': item.grade,
            'price': str(item.price),
            'image': item.slab_image.url if item.slab_image else '',
        }

        messages.success(request, "Added to basket")

    else:

        messages.info(
            request,
            'This item is already in your basket.'
        )

    request.session['basket'] = basket
    request.session.modified = True

    return redirect('game_detail', game_id=item.game.id)


def view_basket(request):

    basket = [int(x) for x in request.session.get('basket', [])]

    items = GradedItem.objects.filter(id__in=basket)

    context = {
        'items': items
    }

    return render(request, 'store/basket.html', context)


def remove_from_basket(request, item_id):

    item_id = int(item_id)
    basket = [int(x) for x in request.session.get('basket', [])]

    item = get_object_or_404(GradedItem, pk=item_id)

    if item_id in basket:

        basket.remove(item_id)

        request.session['toast_item'] = {
            'title': item.game.title,
            'grade': item.grade,
            'price': str(item.price),
            'image': item.slab_image.url if item.slab_image else '',
        }

        messages.error(request, "Removed from basket")

    else:

        messages.info(request, 'Item was not in your basket.')

    request.session['basket'] = basket
    request.session.modified = True

    return redirect('basket_view')