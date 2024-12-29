from rest_framework import viewsets, status,response

from proudct_management.models import Category, Subcategory
from proudct_management.serializers import CategorySerializer, SubCategorySerializer

class CategoryView(viewsets.ModelViewSet):
    serializer_class =CategorySerializer
    queryset = Category.objects.all()
    filterset_fields = ["name"]
    search_fields = ["name"]
    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class SubCategoryView(viewsets.ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = Subcategory.objects.all()
    filterset_fields = ["name", "category"]
    search_fields = ["name", "category__name"]
    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)