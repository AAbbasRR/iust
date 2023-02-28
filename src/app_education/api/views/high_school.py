from rest_framework import generics

from app_education.api.serializers.high_school import (
    HighSchoolSerializer
)

from utils import BaseVersioning
from utils.permissions import IsAuthenticated


class HighSchoolCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = HighSchoolSerializer


class HighSchoolDetailUpdateView(generics.RetrieveUpdateAPIView):
    allowed_methods = ['OPTIONS', 'GET', 'PUT']
    permission_classes = [IsAuthenticated, ]
    versioning_class = BaseVersioning
    serializer_class = HighSchoolSerializer

    def get_object(self):
        return self.request.user.user_high_school
