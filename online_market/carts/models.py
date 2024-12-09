from django.db import models
from django.conf import settings
from products.models import Product  

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart of {self.user.email}"  # Отображение email пользователя в админ-панели

    def get_total(self):
        # Use prefetch_related to optimize queries
        cart_items = self.cartitem_set.prefetch_related('product').all()
        return sum(item.get_cost() for item in cart_items)

    def add_item(self, product, quantity=1):
        cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
        if not created:
            cart_item.quantity += quantity
        cart_item.save()

    def remove_item(self, product):
        CartItem.objects.filter(cart=self, product=product).delete()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"  # Отображение количества и названия товара

    def get_cost(self):
        return self.product.price * self.quantity

     def clean(self):
        if self.quantity < 1:
            raise ValidationError('Quantity must be at least 1')

