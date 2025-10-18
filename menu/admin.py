from django.contrib import admin

from .models import Category, Dish

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'is_popular')
    list_filter = ('category', 'available', 'is_popular')
    search_fields = ('name', 'description', 'ingredients')

