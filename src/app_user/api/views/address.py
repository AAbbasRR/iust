from rest_framework import generics, exceptions

from app_user.models import AddressModel
from app_user.api.serializers.address import (
    AddressSerializer
)

from utils import BaseVersioning
from utils.permissions import IsAuthenticated


class AddressCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = AddressSerializer


class AddressDetailUpdateView(generics.RetrieveUpdateAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT']
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = AddressSerializer

    def get_object(self):
        return self.request.user.user_address
