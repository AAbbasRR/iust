from rest_framework.permissions import (
    AllowAny as AllowAnyPermission,
    IsAuthenticated as IsAuthenticatedPermission,
)
from rest_framework.permissions import BasePermission

from utils import BaseErrors


class IsAdminPermission(BasePermission):
    message = {"status": False, "message": BaseErrors.user_is_not_admin}

    def has_permission(self, request, view):
        try:
            if request.user.is_staff is False:
                return False
            else:
                return True
        except Exception:
            return False
