import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from store.models import GradedItem
from .models import Order, OrderLineItem


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):

        intent = event['data']['object']

        pid = intent.id
        metadata = intent.metadata

        basket = json.loads(metadata.get('basket', '[]'))
        user_id = metadata.get('user_id')

        # prevent duplicates
        if Order.objects.filter(stripe_pid=pid).exists():
            return HttpResponse(status=200)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return HttpResponse(status=400)

        order = Order.objects.create(
            user=user,
            full_name=user.get_full_name() or user.username,
            email=user.email,
            phone_number="",
            street_address1="",
            town_or_city="",
            postcode="",
            country="GB",
            stripe_pid=pid,
            original_basket=json.dumps(basket),
        )

        for item_id in basket:

            try:
                item = GradedItem.objects.get(id=item_id)

                OrderLineItem.objects.create(
                    order=order,
                    graded_item=item,
                    item_price=item.price,
                )

            except GradedItem.DoesNotExist:
                continue

        return HttpResponse(status=200)
    
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)