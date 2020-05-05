from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from game.forms.game_form import GameCreateForm
from game.models import Game, GameImage


# Create your views here.


def index(request):
    cart_id_dict = request.session['cart_id_dict']
    context = {'games': Game.objects.all().order_by('name'), 'cart_id_dict': cart_id_dict}
    return render(request, 'cart/cart_overview.html', context)


def reduce_quantity(request, id):
    cart_id_dict = request.session['cart_id_dict']

    if cart_id_dict[id] == 1:
        del cart_id_dict[id]
    else:
        cart_id_dict[id] -= 1

    request.session['cart_id_dict'] = cart_id_dict

    return redirect('checkout')


def add_quantity(request, id):
    cart_id_dict = request.session['cart_id_dict']

    cart_id_dict[id] += 1

    request.session['cart_id_dict'] = cart_id_dict

    return redirect('checkout')
