# from django.db import models
# from django.conf import settings
# from products.models import Product  

# class Cart(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     items = models.ManyToManyField(Product, through='CartItem')

#     def __str__(self):
#         return f"Cart of {self.user.email}"  # Отображение email пользователя в админ-панели

#     def get_total(self):
#         return sum(item.get_cost() for item in self.cartitem_set.all())

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} x {self.product.name}"  # Отображение количества и названия товара

#     def get_cost(self):
#         return self.product.price * self.quantity
from django.db import models
from django.conf import settings
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')
    updated_at = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('ordered', 'Ordered'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"Cart of {self.user.email}"

    def get_total(self):
        return self.cartitem_set.aggregate(
            total=models.Sum(models.F('quantity') * models.F('product__price'))
        )['total'] or 0

    def add_product(self, product, quantity=1):
        cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
        if not created:
            cart_item.quantity += quantity
        cart_item.save()

    def remove_product(self, product):
        self.cartitem_set.filter(product=product).delete()

    def has_product(self, product):
        return self.cartitem_set.filter(product=product).exists()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_cost(self):
        return self.product.price * self.quantity

    def save(self, *args, **kwargs):
        if self.quantity < 1:
            raise ValueError("Quantity must be at least 1")
        super().save(*args, **kwargs)
