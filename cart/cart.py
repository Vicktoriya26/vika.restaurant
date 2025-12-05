from decimal import Decimal
from django.conf import settings
from menu.models import Dish

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, dish, quantity=1, update_quantity=False):
        """Додає або оновлює товар у кошику"""
        dish_id = str(dish.id)

        # захист від неправильних даних у сесії
        if dish_id in self.cart and not isinstance(self.cart[dish_id], dict):
            self.cart[dish_id] = {'quantity': 0, 'price': str(dish.price)}

        if dish_id not in self.cart:
            self.cart[dish_id] = {'quantity': 0, 'price': str(dish.price)}

        if update_quantity:
            self.cart[dish_id]['quantity'] = quantity
        else:
            self.cart[dish_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, dish):
        dish_id = str(dish.id)
        if dish_id in self.cart:
            del self.cart[dish_id]
            self.save()

    def __iter__(self):
        """Ітерація по товарах у кошику з об’єктами Dish та total_price"""
        dish_ids = self.cart.keys()
        dishes = Dish.objects.filter(id__in=dish_ids)
        for dish in dishes:
            item = self.cart[str(dish.id)]
            if isinstance(item, dict):
                item = item.copy()
                item['dish'] = dish
                item['total_price'] = Decimal(item['price']) * item['quantity']
                yield item

    def __len__(self):
        """Загальна кількість товарів у кошику"""
        return sum(item['quantity'] for item in self.cart.values() if isinstance(item, dict))

    def get_total_price(self):
        """Загальна сума кошика"""
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values() if isinstance(item, dict)
        )

    def clear(self):
        """Очищає кошик"""
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
