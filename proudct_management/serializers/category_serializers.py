from proudct_management.models import Category, Subcategory
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("added_by",)

class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = "__all__"
        read_only_fields = ("added_by",)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = CategorySerializer(instance.category).data
        return data