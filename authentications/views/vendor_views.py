from rest_framework import viewsets, response, status,permissions

from authentications.models import VendorInformation
from authentications.serializers import VendorInformationSerializer
from utils.permissions import IsVendorOrAdmin


class VendorInformationView(viewsets.ModelViewSet):
    serializer_class = VendorInformationSerializer
    queryset = VendorInformation.objects.all()
    permission_classes = [IsVendorOrAdmin]