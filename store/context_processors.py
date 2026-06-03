from .models import GradedItem


def basket_contents(request):
    """
    Makes basket information available
    in every template.
    """

    basket = request.session.get('basket', [])

    basket_count = len(basket)

    basket_total = 0

    items = GradedItem.objects.filter(
        id__in=basket
    )

    for item in items:
        basket_total += item.price

    return {
        'basket_count': basket_count,
        'basket_total': basket_total,
    }