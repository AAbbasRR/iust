from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions

from app_user.models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = (
            "first_name",
            "last_name",
            "birth_date",
            "gender",
            "nationality",
            "mother_language",
            "other_languages",
            "english_status",
            "persian_status",
        )
