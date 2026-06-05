from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'order_number',
        'full_name',
        'email',
        'order_total',
        'created_at',
    )

    readonly_fields = (
        'order_number',
        'created_at',
        'order_total',
    )

    ordering = ('-created_at',)

    search_fields = (
        'order_number',
        'full_name',
        'email',
    )

    list_filter = (
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