from product_management.views import ProductView
from utils.permissions import IsVendorOrAdmin


class VendorProductView(ProductView):
    permission_classes = [IsVendorOrAdmin]
    http_method_names = ['get','put','patch']