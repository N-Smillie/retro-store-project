from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='store'),
    path('<int:game_id>/', views.game_detail, name='game_detail'),
]