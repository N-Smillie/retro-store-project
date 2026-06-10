from .models import GradedItem


def basket_contents(request):
    """
    Makes basket information available
    in every template.
    """

    basket = [int(x) for x in request.session.get('basket', [])]

    basket_count = len(basket)

    if basket:
        items = GradedItem.objects.filter(id__in=basket)
        basket_total = sum(item.price for item in items)
    else:
        items = []
        basket_total = 0

    toast_item = request.session.pop('toast_item', None)

    return {
        'basket_count': basket_count,
        'basket_total': basket_total,
        'toast_item': toast_item,
    }