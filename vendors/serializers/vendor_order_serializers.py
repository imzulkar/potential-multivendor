from rest_framework import serializers
from checkout_management.models import Order, OrderItem, OrderShipping
from checkout_management.serializers import ShippingAddressSerializer


class VendorOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            # "total_cost",
            "status",
            "created_at",
            "updated_at",
        ]


class VendorOrderItemsSerializer(serializers.ModelSerializer):

    order = VendorOrderSerializer(read_only=True)
    # shipping = ShippingAddressSerializer(source="order.shipping", read_only=True)
    class Meta:
        model = OrderItem
        fields = "__all__"