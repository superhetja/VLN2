from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/games
    path('', views.index, name="game-index"),
    path('<int:id>', views.get_game_by_id, name="game-details"),
    path('add_to_cart/<int:id>', views.add_to_cart, name="add_to_cart"),
]