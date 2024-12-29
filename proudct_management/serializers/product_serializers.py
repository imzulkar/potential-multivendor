from rest_framework import serializers

from proudct_management.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # read_only_fields = ('vendor',)