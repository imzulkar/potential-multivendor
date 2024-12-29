from rest_framework import serializers

from authentications.models import User, VendorInformation
from authentications.serializers import UserSerializer


class VendorInformationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = VendorInformation
        fields = "__all__"





