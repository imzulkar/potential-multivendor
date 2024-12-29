from django.urls import path
from rest_framework.routers import DefaultRouter

from authentications.views.vendor_views import VendorInformationView
from vendors.views import VendorProductView
from vendors.views.vendor_analytics_views import VendorAnalytics
from vendors.views.vendor_order_views import VendorOrderItems

router = DefaultRouter()
router.register("profile", VendorInformationView, basename="vendor-profile")
router.register("products", VendorProductView, basename="vendor-products")
router.register("orders", VendorOrderItems, basename="vendor-orders")
urlpatterns = [
    path("analytics/",VendorAnalytics.as_view({'get':"analytics"}))
              ] + router.urls