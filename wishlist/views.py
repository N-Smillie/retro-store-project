from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Wishlist, WishlistItem
from store.models import Game


@login_required
def view_wishlist(request):

    wishlist, created = Wishlist.objects.get_or_create(

        user_profile=request.user.profile

    )

    context = {

        'wishlist_items':

            wishlist.items.select_related(

                'game'

            )

    }

    return render(

        request,

        'wishlist/wishlist.html',

        context

    )


@login_required
def add_to_wishlist(
    request,
    game_id
):

    game = get_object_or_404(
        Game,
        pk=game_id
    )

    wishlist, created = Wishlist.objects.get_or_create(

        user_profile=request.user.profile

    )

    item, created = WishlistItem.objects.get_or_create(

        wishlist=wishlist,

        game=game

    )

    if created:

        messages.success(

            request,

            f'{game.title} added to wishlist.'

        )

    else:

        messages.info(

            request,

            f'{game.title} is already in your wishlist.'

        )

    return redirect(

        'game_detail',

        game_id=game.id

    )


@login_required
def remove_from_wishlist(
    request,
    game_id
):

    game = get_object_or_404(
        Game,
        pk=game_id
    )

    wishlist = request.user.profile.wishlist

    WishlistItem.objects.filter(

        wishlist=wishlist,

        game=game

    ).delete()

    messages.success(

        request,

        f'{game.title} removed from wishlist.'

    )

    return redirect('wishlist')


@login_required
def update_wishlist_notes(

    request,

    item_id

):

    item = get_object_or_404(

        WishlistItem,

        pk=item_id,

        wishlist__user_profile=request.user.profile

    )

    if request.method == 'POST':

        item.notes = request.POST.get(

            'notes',

            ''

        )

        item.save()

        messages.success(

            request,

            'Wishlist notes updated.'

        )

    return redirect('wishlist')
