from rest_framework import serializers
from .models import Cart, CartItem
from products.serializers import ProductSerializer  

class CartItemSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = CartItem
        fields = ['product_details', 'quantity', 'get_cost']
        read_only_fields = ['product_details', 'get_cost']

class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['user', 'items', 'total_price']

     def get_total_price(self, obj):
            total = obj.cartitem_set.aggregate(
                total_price=Sum(F('quantity') * F('product__price'))
            )['total_price']
            return total or 0
    
    
        def get_items(self, obj):
            cart_items = obj.cartitem_set.select_related('product')
            return CartItemSerializer(cart_items, many=True).data
