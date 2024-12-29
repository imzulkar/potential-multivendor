from rest_framework import viewsets, status
from rest_framework.response import Response

from product_management.models import Product
from checkout_management.models import OrderItem, Order
from utils.permissions import IsVendorOrAdmin
from django.db.models import Sum, Count, F

class VendorAnalytics(viewsets.ViewSet):
    permission_classes = [IsVendorOrAdmin]


    def analytics(self, request):
        # Ensure the user is a vendor
        vendor = getattr(request.user, "vendor_information", None)
        if not vendor:
            return Response({"detail": "You are not authorized to access this data."}, status=status.HTTP_403_FORBIDDEN)

        # Total Products Listed
        total_products = Product.objects.filter(vendor=vendor).count()

        # Total Orders Received
        total_orders = Order.objects.filter(items__product__vendor=vendor).distinct().count()

        # Total Revenue Earned
        total_revenue = (
                OrderItem.objects.filter(product__vendor=vendor)
                .aggregate(total=Sum(F("quantity") * F("price")))["total"] or 0
        )

        # Analytics Data
        analytics_data = {
            "total_products": total_products,
            "total_orders": total_orders,
            "total_revenue": total_revenue,
        }

        return Response(analytics_data, status=status.HTTP_200_OK)
