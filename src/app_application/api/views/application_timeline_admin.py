from rest_framework import generics

from app_application.models import TimeLineModel
from app_application.api.serializers.application_timeline_admin import (
    AdminApplicationTimeLineSerializer
)

from utils.permissions import (
    IsAuthenticatedPermission,
    IsAdminPermission
)
from utils.versioning import BaseVersioning
from utils.paginations import BasePagination


class AdminCreateApplicationTimeLineView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = AdminApplicationTimeLineSerializer
    queryset = TimeLineModel.objects.all()

