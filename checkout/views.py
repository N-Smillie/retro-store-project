from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderLineItem
from store.models import GradedItem
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def checkout(request):

    basket = [int(x) for x in request.session.get('basket', [])]

    if not basket:
        return redirect('basket_view')

    items = sorted(
        GradedItem.objects.filter(id__in=basket),
        key=lambda x: basket.index(x.id)
    )

    order_total = sum(item.price for item in items)

    if request.method == 'POST':

        order_form = OrderForm(request.POST)

        if order_form.is_valid():

            order = order_form.save(commit=False)
            order.user = request.user
            order.order_total = order_total
            order.save()

            for item in items:
                OrderLineItem.objects.create(
                    order=order,
                    graded_item=item,
                    item_price=item.price,
                )

            request.session.pop('basket', None)

            messages.success(
                request,
                f'Order {order.order_number} created successfully.'
            )

            return redirect('checkout_success', order_number=order.order_number)

        else:
            messages.error(request, "There was an error with your form. Please check your details.")

    else:
        order_form = OrderForm()

    context = {
        'items': items,
        'order_total': order_total,
        'order_form': order_form,
    }

    return render(request, 'checkout/checkout.html', context)

def checkout_success(request, order_number):

    order = get_object_or_404(Order, order_number=order_number)
    
    request.session.pop('basket', None)

    messages.success(
        request,
        f'Order {order.order_number} completed successfully!'
    )

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)