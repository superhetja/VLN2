from . import views

"""captain_console URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

urlpatterns = [
    path('', views.index, name="checkout"),
    path('reduce_quantity/<int:id>', views.reduce_quantity, name="reduce_quantity"),
    path('add_quantity/<int:id>', views.add_quantity, name="add_quantity"),
    path('contact_info', views.contact_page, name="contact_info"),
    path('payment_details', views.payment_details, name="payment_details"),
    path('review_order', views.review_order, name="review_order"),
    path('payment_confirmed', views.payment_confirmed, name="payment_confirmed")

]

