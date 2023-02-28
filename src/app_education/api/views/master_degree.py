from rest_framework import generics

from app_education.api.serializers.master_degree import (
    MasterDegreeSerializer
)

from utils import BaseVersioning
from utils.permissions import IsAuthenticated


class MasterDegreeCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = MasterDegreeSerializer


class MasterDegreeDetailUpdateView(generics.RetrieveUpdateAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT']
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = MasterDegreeSerializer

    def get_object(self):
        return self.request.user.user_master_degree
