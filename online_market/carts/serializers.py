from rest_framework import serializers
from .models import Cart, CartItem
from products.serializers import ProductSerializer  

class CartItemSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = CartItem
        fields = ['product_details', 'quantity', 'get_cost']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(source='cartitem_set', many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['user', 'items', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total()