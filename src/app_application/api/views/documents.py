from rest_framework import generics

from app_application.api.serializers.documents import (
    DocumentsSerializer
)

from utils import BaseVersioning
from utils.permissions import IsAuthenticated


class DocumentsCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = DocumentsSerializer


class DocumentsDetailUpdateView(generics.RetrieveUpdateAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT']
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = DocumentsSerializer
    lookup_field = 'tracking_id'

    def get_queryset(self):
        return self.request.user.user_application.all()

    def get_object(self):
        obj = super(DocumentsDetailUpdateView, self).get_object()
        return obj.application_document
