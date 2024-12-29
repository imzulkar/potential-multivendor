from django.db.models import Sum, F, Count
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from authentications.models import VendorInformation
from authentications.views.vendor_views import VendorInformationView
from checkout_management.models import Order, OrderItem
from checkout_management.views import OrderView
from product_management.models import Product
from product_management.views import ProductView


class AdminVendorRequest(VendorInformationView):
    permission_classes = [permissions.IsAdminUser]


class AdminProductsView(ProductView):
    permission_classes = [permissions.IsAdminUser]

class AdminOrdersView(OrderView):
    permission_classes = [permissions.IsAdminUser]

class AdminAnalytics(viewsets.ViewSet):

    permission_classes = [permissions.IsAdminUser]

    def analytics(self, request):
        # Ensure the user is a vendor
        vendor = getattr(request.user, "vendor_information", None)
        if not vendor:
            return Response({"detail": "You are not authorized to access this data."}, status=status.HTTP_403_FORBIDDEN)


        total_vendors = VendorInformation.objects.all()
        total_products = Product.objects.all().count()

        summary = Order.objects.aggregate( total_orders=Count('id'), total_revenue=Sum('total_cost') )
        # Analytics Data
        analytics_data = {
            "total_vendors": total_vendors.count(),
            "active_vendors": total_vendors.filter(status="ACTIVE").count(),
            "total_products": total_products,
            "total_orders": summary["total_orders"],
            "total_revenue": summary['total_revenue'],
        }

        return Response(analytics_data, status=status.HTTP_200_OK)