
from django.shortcuts import render, get_object_or_404, redirect
from .models import Dish, Category
from django.db.models import Q

# Сторінка з усіма товарами / пошук
def product_list(request):
    query = request.GET.get('q', '')
    categories = Category.objects.prefetch_related('dishes').all()
    
    if query:
        # Фільтруємо страви за пошуковим запитом
        dishes = Dish.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query),
            available=True
        )
    else:
        # Якщо пошуку немає — показуємо всі доступні страви
        dishes = Dish.objects.filter(available=True)

    return render(request, 'product_list.html', {
        'categories': categories,
        'dishes': dishes,
        'query': query
    })

# Сторінка з деталями однієї страви
def product_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'product_detail.html', {'dish': dish})

# Головна сторінка — популярні страви
def index(request):
    popular_dishes = Dish.objects.filter(is_popular=True, available=True)[:6]
    return render(request, 'index.html', {'popular_dishes': popular_dishes})

