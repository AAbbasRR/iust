from django.contrib.auth import get_user_model

from rest_framework import serializers

from app_user.models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = (
            "id",
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
        extra_kwargs = {
            'id': {'read_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'birth_date': {'required': True},
            'gender': {'required': True},
            'nationality': {'required': True},
            'mother_language': {'required': True},
            'other_languages': {'required': False},
            'english_status': {'required': True},
            'persian_status': {'required': True},
        }

    def __init__(self, *args, **kwargs):
        super(ProfileSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ['PUT', 'PATCH']:
                for field_name, field in self.fields.items():
                    field.required = False

    def create(self, validated_data):
        profile_obj = ProfileModel.objects.create(
            user=self.user,
            **validated_data
        )
        return profile_obj

    def update(self, instance, validated_data):
        for field_name in validated_data:  # update profile fields
            setattr(instance, field_name, validated_data[field_name])
        instance.save()
        return instance
