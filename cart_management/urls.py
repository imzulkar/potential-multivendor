from django.urls import path

from rest_framework.routers import DefaultRouter

from cart_management.views import CartViewSet,CartItemViewSet

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cart-items', CartItemViewSet, basename='cart-item')

urlpatterns = []+router.urls