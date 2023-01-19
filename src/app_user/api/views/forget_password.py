from rest_framework import generics
from rest_framework.response import Response

from app_user.api.serializers.forget_password import (
    ForgetPasswordSerializer,
    ValidateForgetPasswordOTPSerializer,
    CompleteForgetPasswordSerializer
)

from utils import BaseVersioning
from utils.permissions import AllowAny


class ForgetPasswordView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    versioning_class = BaseVersioning
    serializer_class = ForgetPasswordSerializer

    def post(self, request, *args, **kwargs):
        ser = self.serializer_class(data=self.request.data)
        ser.is_valid(raise_exception=True)
        return Response(ser.validated_data)


class ValidateForgetPasswordOTPView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    versioning_class = BaseVersioning
    serializer_class = ValidateForgetPasswordOTPSerializer

    def post(self, request, *args, **kwargs):
        ser = self.serializer_class(data=self.request.data)
        ser.is_valid(raise_exception=True)
        return Response(ser.validated_data)


class CompleteForgetPasswordView(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    versioning_class = BaseVersioning
    serializer_class = CompleteForgetPasswordSerializer

    def post(self, request, *args, **kwargs):
        ser = self.serializer_class(data=self.request.data)
        ser.is_valid(raise_exception=True)
        return Response(ser.validated_data)
