from rest_framework import serializers

from app_frequently_question.models import FrequentlyQuestionModel


class FrequentlyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyQuestionModel
        fields = "__all__"
