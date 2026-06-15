from django.db import models


class Wishlist(models.Model):

    user_profile = models.OneToOneField(
        'profiles.UserProfile',
        on_delete=models.CASCADE,
        related_name='wishlist'
    )

    def __str__(self):

        return (

            f"{self.user_profile.user.username}'s Wishlist"

        )


class WishlistItem(models.Model):

    wishlist = models.ForeignKey(
        Wishlist,
        on_delete=models.CASCADE,
        related_name='items'
    )

    game = models.ForeignKey(
        'store.Game',
        on_delete=models.CASCADE
    )

    notes = models.TextField(
        blank=True,
        max_length=500
    )

    added_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        unique_together = (

            'wishlist',
            'game'

        )

    def __str__(self):

        return (

            self.game.title

        )