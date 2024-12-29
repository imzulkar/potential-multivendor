from django.urls import path

from rest_framework.routers import DefaultRouter

from admin_dashboard.views import AdminVendorRequest, AdminProductsView, AdminOrdersView, AdminAnalytics

router = DefaultRouter()
router.register("vendors",AdminVendorRequest, basename="vendors")
router.register("products",AdminProductsView, basename="products")
router.register("orders",AdminOrdersView, basename="Orders")
urlpatterns = [
    path("analytics/", AdminAnalytics.as_view({'get': "analytics"}))
              ]+router.urls