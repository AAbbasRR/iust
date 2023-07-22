from rest_framework import generics

from app_application.api.serializers.application import ApplicationSerializer

from utils.versioning import BaseVersioning
from utils.paginations import BasePagination
from utils.permissions import IsAuthenticatedPermission


class ListAllApplicationsView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedPermission, ]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return self.request.user.user_application.all()


class ApplicationCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedPermission, ]
    versioning_class = BaseVersioning
    serializer_class = ApplicationSerializer


class ApplicationDetailUpdateView(generics.RetrieveUpdateAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT']
    permission_classes = [IsAuthenticatedPermission, ]
    versioning_class = BaseVersioning
    serializer_class = ApplicationSerializer
    lookup_field = 'tracking_id'

    def get_queryset(self):
        return self.request.user.user_application.all()
