from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from menu.models import Dish
from django.shortcuts import redirect

def cart_clear(request):
    request.session['cart'] = {}
    request.session.modified = True
    return redirect('cart:cart_detail')  # або куди хочеш перенаправляти


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


def cart_add(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Dish, id=product_id)
    product_id_str = str(product.id)

    if product_id_str in cart:
        cart[product_id_str]['quantity'] += 1
    else:
        cart[product_id_str] = {'quantity': 1, 'price': str(product.price)}

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('menu:product_list')



def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Dish, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_update_quantity(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Dish, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity, update_quantity=True)
    return redirect('cart_detail')
