from rest_framework import generics

from app_application.api.serializers.documents import DocumentsSerializer

from utils import BaseVersioning
from utils.permissions import IsAuthenticatedPermission


class DocumentsCreateView(generics.CreateAPIView):
    permission_classes = [
        IsAuthenticatedPermission,
    ]
    versioning_class = BaseVersioning
    serializer_class = DocumentsSerializer


class DocumentsDetailUpdateView(generics.RetrieveUpdateAPIView):
    allowed_methods = ["OPTIONS", "GET", "PUT"]
    permission_classes = [
        IsAuthenticatedPermission,
    ]
    versioning_class = BaseVersioning
    serializer_class = DocumentsSerializer
    lookup_field = "pk"

    def get_queryset(self):
        if self.request.user.is_agent:
            return self.request.user.agent_applications.application_document.all()
        else:
            return self.request.user.user_documents.all()
