from rest_framework import generics

from app_application.models import ApplicationModel
from app_application.api.serializers.application_admin import (
    AdminApplicationListSerializer,
    AdminDetailApplicationSerializer
)
from app_application.filters.applications import ApplicationListFilter

from utils.permissions import (
    IsAuthenticatedPermission,
    IsAdminPermission
)
from utils.versioning import BaseVersioning
from utils.paginations import BasePagination


class AdminAllApplicationView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = AdminApplicationListSerializer
    ordering_fields = ["create_at"]
    filterset_class = ApplicationListFilter
    queryset = ApplicationModel.objects.all()


class AdminDetailApplicationView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminPermission]
    versioning_class = BaseVersioning
    serializer_class = AdminDetailApplicationSerializer
    queryset = ApplicationModel.objects.all()
    lookup_field = "pk"
