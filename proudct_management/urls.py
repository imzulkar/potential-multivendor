from django.urls import path

from rest_framework.routers import DefaultRouter

from proudct_management.views import CategoryView, SubCategoryView
from proudct_management.views.product_views import ProductView

router = DefaultRouter()
router.register("category",  CategoryView, basename="category")
router.register("sub-category",  SubCategoryView, basename="sub_category")
router.register("",  ProductView, basename="product")


urlpatterns = [

]+router.urls