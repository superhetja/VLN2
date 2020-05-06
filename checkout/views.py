from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from game.forms.game_form import GameCreateForm
from game.models import Game, GameImage
from django import forms
from checkout.forms.contact_info_form import ContactForm


# Create your views here.

def contact_page(request):
    contact = ContactForm()
    return render(request, "checkout/contact_info.html", {'form': contact})


def payment_details(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            request.session['contact_info'] = form.cleaned_data
            print(request.session['contact_info'])
            return render(request, 'checkout/payment_details.html')
        else:
            return redirect('contact_info')


def index(request):
    cart_id_dict = request.session.get('cart_id_dict', {})
    if len(cart_id_dict) == 0:
        return render(request, 'cart/cart_empty.html')
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
