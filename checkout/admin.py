from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'email',
        'created_at',
    )

    inlines = [OrderLineItemInline]


@admin.register(OrderLineItem)
class OrderLineItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'graded_item',
        'item_price',
    )