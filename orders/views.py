
from django.shortcuts import render, redirect
from django.http import HttpResponse

def cart_detail(request):
    return HttpResponse("Сторінка кошика")

def add_to_cart(request, dish_id):
    return HttpResponse(f"Страву додано до кошика! {dish_id}")

def remove_from_cart(request, dish_id):
    return HttpResponse(f"Видалено страву з ID {dish_id}")

def checkout(request):
    return HttpResponse("Оформлення замовлення")

