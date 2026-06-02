from django.shortcuts import render, redirect
from .models import Order, OrderLineItem
from store.models import GradedItem

def checkout(request):

    basket = request.session.get('basket', [])

    if not basket:
        return redirect('basket_view')

    items = GradedItem.objects.filter(id__in=basket)

    context = {
        'items': items,
    }

    return render(
        request,
        'checkout/checkout.html',
        context
    )