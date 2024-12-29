from authentications.models import VendorInformation
from rest_framework import serializers


class VendorIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorInformation
        fields = ["id"]