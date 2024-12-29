from rest_framework import viewsets, status, permissions

from proudct_management.helper.product_filter import ProductFilter
from proudct_management.models import  Product, Category, Subcategory
from proudct_management.serializers import  ProductSerializer
from utils.permissions import  IsVendorOrAdminOrReadOnly




class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related("category", "subcategory__category", "vendor__user")
    serializer_class =ProductSerializer

    permission_classes = [IsVendorOrAdminOrReadOnly]
    filterset_class = ProductFilter
    filterset_fields = ["vendor", "category", "subcategory", "name"]
    search_fields = ["vendor", "category", "subcategory", "name","vendor__business_name", "category__name", "subcategory__name"]
    # /products/?min_price=100&max_price=500
    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            serializer.save()
        else:
            serializer.save(vendor = self.request.user.vendor_information)

