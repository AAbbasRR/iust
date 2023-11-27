from django.utils.translation import gettext as _

from rest_framework import generics, response, status, exceptions

from app_notification.api.serializers.notification import NotificationSerializer
from app_notification.models import NotificationModel

from utils.base_errors import BaseErrors
from utils.versioning import BaseVersioning
from utils.paginations import BasePagination
from utils.permissions import IsAuthenticatedPermission


class ListNotificationView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return NotificationModel.objects.filter(user=self.request.user)


class ViewNotificationView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission]
    versioning_class = BaseVersioning
    lookup_field = "pk"

    def get_queryset(self):
        return NotificationModel.objects.filter(user=self.request.user)

    def get_object(self):
        pk_param_value = self.request.GET.get(self.lookup_field, None)
        if pk_param_value is None or pk_param_value == "":
            raise exceptions.ParseError(
                BaseErrors._change_error_variable(
                    "parameter_is_required", param_name="pk"
                )
            )
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.filter(pk=pk_param_value).first()
        if obj is None:
            raise exceptions.NotFound(
                BaseErrors._change_error_variable(
                    "object_not_found", object=_("Notification")
                )
            )
        return obj

    def get(self, *args, **kwargs):
        notification_object = self.get_object()
        notification_object.view_message()
        return response.Response(
            {"message": BaseErrors.message_success_viewed}, status=status.HTTP_200_OK
        )
