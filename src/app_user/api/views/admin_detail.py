from rest_framework import generics, response

from app_application.models import ReferralModel

from utils.permissions import IsAuthenticatedPermission, IsAdminUserPermission
from utils.versioning import BaseVersioning


class AdminDetailDataView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning

    def get(self, *args, **kwargs):
        return response.Response(
            {
                "referral_count": ReferralModel.objects.filter(
                    destination_user=self.request.user, is_enabled=True
                ).count()
            }
        )
