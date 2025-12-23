from django.shortcuts import render, get_object_or_404, redirect
from menu.models import Dish
from .cart import Cart

def cart_add(request, dish_id):
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    cart.add(dish=dish)
    return redirect('cart:detail')

def cart_remove(request, dish_id):
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    cart.remove(dish)
    return redirect('cart:detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:detail')
