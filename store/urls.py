from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='store'),
    path('<int:game_id>/', views.game_detail, name='game_detail'),
    path('basket/', views.view_basket, name='basket_view'),
    path('basket/add/<int:item_id>/', views.add_to_basket, name='add_to_basket'),
]