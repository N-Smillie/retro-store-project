import uuid

from django.db import models
from django.contrib.auth.models import User

from store.models import GradedItem

class Order(models.Model):

    order_number = models.CharField(
        max_length=32,
        editable=False,
        unique=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):

        if not self.order_number:
            self.order_number = (
                self._generate_order_number()
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
    

class OrderLineItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )

    graded_item = models.ForeignKey(
        GradedItem,
        on_delete=models.CASCADE
    )

    item_price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    def __str__(self):

        return (
            f"{self.graded_item.game.title}"
            f" ({self.graded_item.grade})"
        )
