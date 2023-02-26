from rest_framework import generics

from app_user.models import ProfileModel
from app_user.api.serializers.profile import (
    ProfileSerializer
)

from utils import BaseVersioning
from utils.permissions import IsAuthenticated


class ProfileCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = ProfileSerializer


class ProfileDetailUpdateView(generics.RetrieveUpdateAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT']
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.user_profile
