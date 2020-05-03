from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/users
    path('', views.index, name="user-index"),
    path('signup', views.create_user, name="create_user"),
    path('update_user/<int:id>', views.update_user, name="update_user")
]