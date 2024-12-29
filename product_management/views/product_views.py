from rest_framework import viewsets, status, permissions

from product_management.helper.product_filter import ProductFilter
from product_management.models import  Product, Category, Subcategory
from product_management.serializers import  ProductSerializer
from utils.permissions import  IsVendorOrAdminOrReadOnly




class ProductView(viewsets.ModelViewSet):
    # queryset = Product.objects.all().select_related("category", "subcategory__category", "vendor__user")
    serializer_class =ProductSerializer

    permission_classes = [IsVendorOrAdminOrReadOnly]
    filterset_class = ProductFilter
    filterset_fields = ["vendor", "category", "subcategory", "name"]
    search_fields = ["vendor", "category", "subcategory", "name","vendor__business_name", "category__name", "subcategory__name"]

    def get_queryset(self):
        if req_user := self.request.user.role == "VENDOR":
            vendor_user = self.request.user.vendor_information
            return Product.objects.filter(vendor=vendor_user).select_related("category", "subcategory__category", "vendor__user")
        return Product.objects.all().select_related("category", "subcategory__category", "vendor__user")
    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            serializer.save()
        else:
            serializer.save(vendor = self.request.user.vendor_information)

