from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.apps import apps
from django.dispatch import receiver


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    default_phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    default_street_address1 = models.CharField(
        max_length=100,
        blank=True
    )

    default_street_address2 = models.CharField(
        max_length=100,
        blank=True
    )

    default_town_or_city = models.CharField(
        max_length=50,
        blank=True
    )

    default_postcode = models.CharField(
        max_length=20,
        blank=True
    )

    default_county = models.CharField(
        max_length=50,
        blank=True
    )

    default_country = models.CharField(
        max_length=50,
        blank=True
    )

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_or_update_user_profile(
    sender,
    instance,
    created,
    **kwargs
):
    """
    Create or update the user profile
    and wishlist.
    """

    profile, created = UserProfile.objects.get_or_create(
        user=instance
    )

    Wishlist = apps.get_model(
        'wishlist',
        'Wishlist'
    )

    Wishlist.objects.get_or_create(
        user_profile=profile
    )

    profile.save()