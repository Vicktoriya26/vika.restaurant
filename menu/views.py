
from django.shortcuts import render, get_object_or_404, redirect
from .models import Dish, Category
from django.db.models import Q

def product_list(request):
    q = request.GET.get('q', '')
    if q:
        dishes = Dish.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
    else:
        dishes = Dish.objects.filter(available=True).order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'product_list.html', {'dishes': dishes, 'categories': categories, 'q': q})

def product_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'product_detail.html', {'dish': dish})

