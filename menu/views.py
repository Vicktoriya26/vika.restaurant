
from django.shortcuts import render, get_object_or_404, redirect
from .models import Dish, Category
from django.db.models import Q

def product_list(request):
    query = request.GET.get('q')
    categories = Category.objects.prefetch_related('dishes').all()
    
    if query:
        dishes = Dish.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query),
            available=True
        )

    return render(request, 'product_list.html', {
        'categories': categories,
        'dishes': dishes if query else None,
        'query': query or ''
    })


def product_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'product_detail.html', {'dish': dish})

def index(request):
    popular_dishes = Dish.objects.filter(is_popular=True, available=True)[:6]
    return render(request, 'index.html', {'popular_dishes': popular_dishes})

