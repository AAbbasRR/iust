from rest_framework import generics

from app_occupation.api.serializers.latest_occupation import LatestOccupationSerializer

from utils import BaseVersioning
from utils.permissions import IsAuthenticatedPermission


class LatestOccupationDetailUpdateView(generics.RetrieveUpdateAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT']
    permission_classes = [IsAuthenticatedPermission, ]
    versioning_class = BaseVersioning
    serializer_class = LatestOccupationSerializer

    def get_object(self):
        return self.request.user.user_latest_occupation
