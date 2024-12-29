from django.urls import path

from rest_framework.routers import DefaultRouter

from checkout_management.views.checkout_views import OrderView

router = DefaultRouter()
router.register("orders", OrderView, basename="order")

urlpatterns = [

    path("/",OrderView.as_view({"post":"checkout"}) )
              ]+router.urls