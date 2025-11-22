from django.shortcuts import render, redirect, get_object_or_404
from menu.models import Dish


def add_to_cart(request, dish_id):
    """Додає страву до кошика"""
    dish = get_object_or_404(Dish, id=dish_id)

    cart = request.session.get('cart', {})

    # Якщо страва вже у кошику – збільшуємо кількість
    if str(dish_id) in cart:
        cart[str(dish_id)] += 1
    else:
        cart[str(dish_id)] = 1

    request.session['cart'] = cart
    return redirect('cart:cart_detail')


def remove_from_cart(request, dish_id):
    """Видаляє страву повністю"""
    cart = request.session.get('cart', {})

    if str(dish_id) in cart:
        del cart[str(dish_id)]

    request.session['cart'] = cart
    return redirect('cart:cart_detail')


def update_quantity(request, dish_id):
    """Змінює кількість"""
    cart = request.session.get('cart', {})

    qty = int(request.POST.get('quantity', 1))

    if qty > 0:
        cart[str(dish_id)] = qty
    else:
        del cart[str(dish_id)]

    request.session['cart'] = cart
    return redirect('cart:cart_detail')


def cart_detail(request):
    """Показує вміст кошика"""
    cart = request.session.get('cart', {})

    items = []
    total_price = 0

    for dish_id, quantity in cart.items():
        dish = get_object_or_404(Dish, id=dish_id)
        price = dish.price * quantity
        total_price += price

        items.append({
            'dish': dish,
            'quantity': quantity,
            'price': price,
        })

    return render(request, 'cart/cart_detail.html', {
        'items': items,
        'total_price': total_price
    })

