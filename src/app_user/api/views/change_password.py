from django.utils.translation import gettext as _

from rest_framework import generics, response, status

from app_user.api.serializers.change_password import ChangePasswordSerializer

from utils.permissions import (
    IsAuthenticatedPermission,
)


class ChangePasswordView(generics.UpdateAPIView):
    allowed_methods = ["OPTIONS", "PUT"]
    permission_classes = [
        IsAuthenticatedPermission,
    ]
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(
                {"detail": _("Change password Successfully")}, status=status.HTTP_200_OK
            )
