from rest_framework import generics, exceptions

from app_application.api.serializers.application import (
    ApplicationSerializer
)

from utils import BaseVersioning
from utils.permissions import IsAuthenticated


class ListAllApplicationsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return self.request.user.user_application.all()


class ApplicationCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = ApplicationSerializer


class ApplicationDetailUpdateView(generics.RetrieveUpdateAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT']
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = ApplicationSerializer
    lookup_field = 'tracking_id'

    def get_queryset(self):
        return self.request.user.user_application.all()
