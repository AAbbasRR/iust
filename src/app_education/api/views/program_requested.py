from rest_framework import generics

from app_education.api.serializers.program_requested import (
    ProgramRequestedSerializer
)

from utils import BaseVersioning
from utils.permissions import IsAuthenticated


class ProgramRequestedCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = ProgramRequestedSerializer


class ProgramRequestedDetailUpdateView(generics.RetrieveUpdateAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT']
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = ProgramRequestedSerializer
    lookup_field = 'tracking_id'

    def get_queryset(self):
        return self.request.user.user_application.all()

    def get_object(self):
        obj = super(ProgramRequestedDetailUpdateView, self).get_object()
        return obj.application_program_requested
