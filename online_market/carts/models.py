from django.db import models
from django.conf import settings
from products.models import Product  

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart of {self.user.email}"  # Отображение email пользователя в админ-панели

    def get_total(self):
        return sum(item.get_cost() for item in self.cartitem_set.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"  # Отображение количества и названия товара

    def get_cost(self):
        return self.product.price * self.quantity
