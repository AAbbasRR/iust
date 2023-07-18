from rest_framework import generics

from app_occupation.api.serializers.latest_occupation import (
    LatestOccupationSerializer
)

from utils import BaseVersioning
from utils.permissions import IsAuthenticatedPermission


class LatestOccupationCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedPermission, ]
    versioning_class = BaseVersioning
    serializer_class = LatestOccupationSerializer


class LatestOccupationDetailUpdateView(generics.RetrieveUpdateAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT']
    permission_classes = [IsAuthenticatedPermission, ]
    versioning_class = BaseVersioning
    serializer_class = LatestOccupationSerializer
    lookup_field = 'tracking_id'

    def get_queryset(self):
        return self.request.user.user_application.all()

    def get_object(self):
        obj = super(LatestOccupationDetailUpdateView, self).get_object()
        return obj.application_latest_occupation
