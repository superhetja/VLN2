from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/users
    path('', views.index, name="game-index"),
    path('<int:id>', views.get_game_by_id, name="game-details")
]