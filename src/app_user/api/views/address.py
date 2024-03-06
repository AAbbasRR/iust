from rest_framework import generics

from app_user.api.serializers.address import AddressSerializer

from utils import BaseVersioning
from utils.permissions import IsAuthenticatedPermission


class AddressDetailUpdateView(generics.RetrieveUpdateAPIView):
    allowed_methods = ["OPTIONS", "GET", "PUT"]
    permission_classes = [
        IsAuthenticatedPermission,
    ]
    versioning_class = BaseVersioning
    serializer_class = AddressSerializer

    def get_object(self):
        return self.request.user.user_address
