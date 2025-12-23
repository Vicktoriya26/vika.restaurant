from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категорія")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")


    class Meta:
        ordering = ['order']
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва страви")
    description = models.TextField(blank=True, verbose_name="Опис")
    ingredients = models.TextField(blank=True, verbose_name="Інгредієнти")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ціна (₴)")
    image = models.ImageField(upload_to='dishes/', blank=True, null=True, verbose_name="Фото")
    available = models.BooleanField(default=True, verbose_name="Наявність")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes', verbose_name="Категорія")
    is_popular = models.BooleanField(default=False, verbose_name="Популярна страва")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")

    class Meta:
        verbose_name = "Страва"
        verbose_name_plural = "Страви"

    def __str__(self):
        return self.name

