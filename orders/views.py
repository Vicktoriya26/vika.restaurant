
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from orders.forms import ReviewForm
from .models import Order
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from menu.models import Dish 

def cart_detail(request):
    return HttpResponse("Сторінка кошика")

def add_to_cart(request, dish_id):
    return HttpResponse(f"Страву додано до кошика! {dish_id}")

def remove_from_cart(request, dish_id):
    return HttpResponse(f"Страву видалено! {dish_id}")

def checkout(request):
    return HttpResponse("Оформлення замовлення")


def checkout(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        address = request.POST.get("address")
        payment_method = request.POST.get("payment_method")

        order_data = {
            "name": name,
            "phone": phone,
            "city": city,
            "address": address,
            "payment_method": payment_method,
        }

        # Передаємо дані на сторінку підтвердження
        return render(request, "order_confirm.html", {"order": order_data})

    return render(request, "order_form.html")

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/order_history.html", {"orders": orders})

@login_required
def repeat_order(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    cart = Cart(request)

    for item in order.items.all():
        cart.add(
            product_id=None,  # якщо у тебе продукти є в базі — вставимо id
            name=item.product_name,
            price=float(item.price),
            quantity=item.quantity
        )

    return redirect("cart:cart_detail")

@login_required
def add_review(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.dish = dish
            review.save()
            return redirect('dish_detail', dish_id=dish.id)
    else:
        form = ReviewForm()

    return render(request, 'orders/add_review.html', {'form': form, 'dish': dish})