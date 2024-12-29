import django_filters

from product_management.models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    vendor = django_filters.CharFilter(field_name="vendor", lookup_expr="exact")
    category = django_filters.CharFilter(field_name="category", lookup_expr="exact")
    subcategory = django_filters.CharFilter(field_name="subcategory", lookup_expr="exact")
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ["vendor", "category", "subcategory", "name", "min_price", "max_price"]