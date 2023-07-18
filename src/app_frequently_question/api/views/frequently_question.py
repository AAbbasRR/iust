from rest_framework import generics

from app_frequently_question.api.serializers.frequently_question import FrequentlyQuestionSerializer
from app_frequently_question.models import FrequentlyQuestionModel

from utils.versioning import BaseVersioning
from utils.paginations import BasePagination
from utils.permissions import IsAuthenticatedPermission


class FrequentlyQuestionView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = FrequentlyQuestionSerializer
    queryset = FrequentlyQuestionModel.objects.all()
