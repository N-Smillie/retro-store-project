from django.contrib import admin
from .models import Game, GradedItem

# Register your models here.
class GradedItemInline(admin.TabularInline):
    model = GradedItem
    extra = 1


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'console', 'genre')
    list_filter = ('console', 'genre')
    search_fields = ('title',)
    inlines = [GradedItemInline]


@admin.register(GradedItem)
class GradedItemAdmin(admin.ModelAdmin):
    list_display = ('game', 'grade', 'price', 'stock', 'is_available')
    list_filter = ('grade', 'is_available')
    search_fields = ('game__title',)