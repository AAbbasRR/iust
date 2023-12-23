from rest_framework import generics

from app_application.api.serializers.application_timeline_admin import (
    AdminApplicationTimeLineSerializer,
)

from utils.permissions import IsAuthenticatedPermission, IsAdminUserPermission
from utils.versioning import BaseVersioning
from utils.paginations import BasePagination


class AdminCreateApplicationTimeLineView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning
    serializer_class = AdminApplicationTimeLineSerializer
