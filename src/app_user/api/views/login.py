from rest_framework import generics
from rest_framework.response import Response

from app_user.api.serializers.login import (
    UserLoginSerializer
)

from utils import BaseVersioning
from utils.permissions import AllowAny


class UserLoginView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    versioning_class = BaseVersioning
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        ser = self.serializer_class(data=self.request.data)
        ser.is_valid(raise_exception=True)
        return Response(ser.validated_data)
