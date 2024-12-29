from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

# from django.contrib.auth import login
from authentications.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer