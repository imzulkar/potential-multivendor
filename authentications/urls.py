from django.urls import path

from rest_framework.routers import DefaultRouter
from authentications.views import UserRegistrationView, CustomTokenObtainPairView
from authentications.views.vendor_views import VendorInformationView

router = DefaultRouter()

router.register("register", UserRegistrationView, basename="register")
router.register("vendor", VendorInformationView, basename="vendor")
urlpatterns = [
    path("token/",CustomTokenObtainPairView.as_view(), name='user-login')]+router.urls