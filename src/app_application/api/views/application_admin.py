from django.http import HttpResponse

from rest_framework import generics

from app_application.models import ApplicationModel
from app_application.api.serializers.application_admin import (
    AdminApplicationListSerializer,
    AdminApplicationExportResource,
    AdminDetailApplicationSerializer,
)
from app_application.filters.applications import ApplicationListFilter

from utils.permissions import IsAuthenticatedPermission, IsAdminUserPermission
from utils.versioning import BaseVersioning
from utils.paginations import BasePagination


class AdminAllApplicationView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = AdminApplicationListSerializer
    ordering_fields = ["create_at"]
    search_fields = [
        "tracking_id",
        "user__user_profile__first_name",
        "user__user_profile__last_name",
    ]
    filterset_class = ApplicationListFilter
    queryset = ApplicationModel.objects.all()


class AdminExportApplicationListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning
    ordering_fields = ["create_at"]
    search_fields = [
        "tracking_id",
        "user__user_profile__first_name",
        "user__user_profile__last_name",
    ]
    filterset_class = ApplicationListFilter
    queryset = ApplicationModel.objects.all()

    def get(self, *args, **kwargs):
        resource_class = AdminApplicationExportResource()
        dataset = resource_class.export(self.get_queryset())

        response = HttpResponse(dataset.xlsx, content_type="text/xlsx")
        response["Content-Disposition"] = 'attachment; filename="export_orders.xlsx"'
        return response


class AdminDetailApplicationView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning
    serializer_class = AdminDetailApplicationSerializer
    queryset = ApplicationModel.objects.all()
    lookup_field = "pk"
