
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:dish_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
]
