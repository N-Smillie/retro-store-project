from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.view_wishlist,
        name='wishlist'
    ),

    path(
        'add/<int:game_id>/',
        views.add_to_wishlist,
        name='add_to_wishlist'
    ),

    path(
        'remove/<int:game_id>/',
        views.remove_from_wishlist,
        name='remove_from_wishlist'
    ),

    path(
        'notes/<int:item_id>/',
        views.update_wishlist_notes,
        name='update_wishlist_notes'
    ),

]
