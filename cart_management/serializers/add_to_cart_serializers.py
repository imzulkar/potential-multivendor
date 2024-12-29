from rest_framework import serializers
from product_management.models import Product
from cart_management.models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source="product.name")
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = ["id", "product", "product_name", "quantity", "total_price"]

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "user", "items", "total_cost"]
        read_only_fields = ["user"]

    def get_total_cost(self, obj):
        return sum(item.total_price for item in obj.items.all())
