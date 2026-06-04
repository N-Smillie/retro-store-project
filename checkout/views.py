from django.shortcuts import render, redirect
from .models import Order, OrderLineItem
from store.models import GradedItem
from .forms import OrderForm
from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):

    basket = request.session.get('basket', [])

    if not basket:
        return redirect('basket_view')

    items = GradedItem.objects.filter(id__in=basket)

    order_total = 0

    for item in items:
        order_total += item.price

    order_form = OrderForm()

    context = {
        'items': items,
        'order_total': order_total,
        'order_form': order_form,
    }

    return render(
        request,
        'checkout/checkout.html',
        context
    )