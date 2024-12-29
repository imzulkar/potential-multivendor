from django.db import transaction
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from cart_management.models import Cart
from checkout_management.serializers import CheckoutSerializer, OrderSerializer
from checkout_management.models import Order, OrderItem, OrderShipping


class OrderView(viewsets.ModelViewSet):
    """
    ViewSet to manage orders.
    """
    queryset = Order.objects.prefetch_related("items__product").all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "checkout":
            return CheckoutSerializer
        return OrderSerializer

    def get_queryset(self):
        # Users can only view their own orders
        if self.request.user.is_superuser:
            return Order.objects.all()
        if self.request.user.role== "VENDOR":
            Order.objects.filter(items__product__vendor= self.request.user.vendor_information)
        return Order.objects.filter(user=self.request.user)

    def checkout(self, request, *args, **kwargs):

        cart = Cart.objects.filter(user=request.user).prefetch_related("items__product").first()

        if not cart or not cart.items.exists():
            return Response({"error": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            # Create Order
            order = Order.objects.create(
                user=request.user,

            )
            print()
            # shipping address
            shipping_name=serializer.validated_data.get("shipping_name"),
            shipping_address=serializer.validated_data.get("shipping_address"),
            shipping_phone=serializer.validated_data.get("shipping_phone"),
            print(shipping_name, shipping_address, shipping_phone)
            shipping = self._shipping_address(order,shipping_name,shipping_address,shipping_phone)

            total_cost = 0

            if cart_ids := request.data.get("cart_items", None):
                items = cart.items.filter(id__in = cart_ids)
            else:
                items = cart.items.all()
            for cart_item in items:
                # Validate stock
                if cart_item.product.stock_quantity < cart_item.quantity:
                    return Response(
                        {
                            "error": f"Insufficient stock for {cart_item.product.name}. Available: {cart_item.product.stock_quantity}"
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                # Deduct stock
                cart_item.product.stock_quantity -= cart_item.quantity
                cart_item.product.save()

                # Create OrderItem
                order_item = OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price,
                )

                total_cost += order_item.price * order_item.quantity

            # Update Order total cost
            order.total_cost = total_cost
            order.save()

            # Clear Cart
            items.delete()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


    def _shipping_address(self, order, name, address, phone):
        return OrderShipping.objects.create(shipping_address=address, shipping_name=name, shipping_phone=phone, order=order)
