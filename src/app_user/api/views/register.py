from rest_framework import generics
from rest_framework.response import Response

from app_user.api.serializers.register import (
    UserRegisterSerializer,
    UserVerifyRegisterSerializer,
    UserReSendRegisterOTPCodeSerializer
)

from utils import BaseVersioning
from utils.permissions import AllowAny


class UserRegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    versioning_class = BaseVersioning
    serializer_class = UserRegisterSerializer


class UserVerifyRegisterView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    versioning_class = BaseVersioning
    serializer_class = UserVerifyRegisterSerializer

    def post(self, request, *args, **kwargs):
        ser = self.serializer_class(data=self.request.data)
        ser.is_valid(raise_exception=True)
        return Response(ser.validated_data)


class UserReSendRegisterOTPCodeView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    versioning_class = BaseVersioning
    serializer_class = UserReSendRegisterOTPCodeSerializer

    def post(self, request, *args, **kwargs):
        ser = self.serializer_class(data=self.request.data)
        ser.is_valid(raise_exception=True)
        return Response(ser.validated_data)
