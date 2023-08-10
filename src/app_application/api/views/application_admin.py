from rest_framework import generics

from app_application.models import ApplicationModel
from app_application.api.serializers.application_admin import AdminApplicationListSerializer

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
    queryset = ApplicationModel.objects.all()
