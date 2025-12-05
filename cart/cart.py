from decimal import Decimal
from django.conf import settings
from menu.models import Dish

class Cart:
    def __init__(self, request):
        """
        Ініціалізація кошика з сесії
        """
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            # якщо кошика немає в сесії, створюємо порожній
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Додати або оновити товар у кошику
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # зберігаємо зміни в сесії
        self.session.modified = True

    def remove(self, product):
        """
        Видалити товар з кошика
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        # Очистити кошик
        self.session['cart'] = {}
        self.save()

    def __iter__(self):
        """
        Ітеруємо по товарах у кошику та додаємо об'єкт продукту
        """
        product_ids = self.cart.keys()
        products = Dish.objects.filter(id__in=product_ids)
        cart_copy = self.cart.copy()
        for product in products:
            item = cart_copy[str(product.id)]
            item['product'] = product
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Повертає загальну кількість товарів у кошику
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Повертає загальну суму кошика
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
