from rest_framework import generics, response

from app_application.api.serializers.referral_admin import AdminCreateReferralSerializer

from utils.permissions import IsAuthenticatedPermission, IsAdminUserPermission
from utils.versioning import BaseVersioning


class AdminCreateReferralAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning
    serializer_class = AdminCreateReferralSerializer

    def post(self, request, *args, **kwargs):
        ser = self.serializer_class(
            data=self.request.data, context={"request": request}
        )
        ser.is_valid(raise_exception=True)
        return response.Response(ser.validated_data)
