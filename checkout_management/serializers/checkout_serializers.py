from rest_framework import serializers
from checkout_management.models import Order, OrderItem,OrderShipping
from product_management.models import Product


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderShipping
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source="product.name")

    class Meta:
        model = OrderItem
        fields = ["id", "product", "product_name", "quantity", "price"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    # shipping =ShippingAddressSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "total_cost",
            "status",
            "items",
            "shipping",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["user", "status", "total_cost", "created_at", "updated_at"]
        


class CheckoutSerializer(serializers.Serializer):
    shipping_name = serializers.CharField(max_length=255)
    shipping_address = serializers.CharField()
    shipping_phone = serializers.CharField(max_length=15)
    cart_items = serializers.ListSerializer(child=serializers.IntegerField(), required=False)
