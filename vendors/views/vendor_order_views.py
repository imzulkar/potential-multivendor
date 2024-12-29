from rest_framework import viewsets
from checkout_management.models import Order, OrderItem, OrderShipping
from utils.permissions import IsVendorOrAdmin
from vendors.serializers import VendorOrderItemsSerializer

class VendorOrderItems(viewsets.ModelViewSet):
    serializer_class = VendorOrderItemsSerializer
    permission_classes = [IsVendorOrAdmin]
    http_method_names = ['get', "put", "patch"]
    def get_queryset(self):
        if self.request.user.is_superuser:
            return OrderItem.objects.all()
        vendor = self.request.user.vendor_information
        return OrderItem.objects.filter(product__vendor=vendor)
