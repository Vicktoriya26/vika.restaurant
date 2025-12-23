from django.contrib import admin


from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('dish', 'user', 'rating', 'is_active')
    list_filter = ('is_active', 'rating')
