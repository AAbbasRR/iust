from rest_framework import generics

from app_education.api.serializers.bachelor_degree import (
    BachelorDegreeSerializer
)

from utils import BaseVersioning
from utils.permissions import IsAuthenticatedPermission


class BachelorDegreeCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedPermission, ]
    versioning_class = BaseVersioning
    serializer_class = BachelorDegreeSerializer


class BachelorDegreeDetailUpdateView(generics.RetrieveUpdateAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT']
    permission_classes = [IsAuthenticatedPermission, ]
    versioning_class = BaseVersioning
    serializer_class = BachelorDegreeSerializer

    def get_object(self):
        return self.request.user.user_bachelor_degree
