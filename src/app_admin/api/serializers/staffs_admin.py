from rest_framework import serializers

from app_admin.models import AdminModel
from app_user.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField("get_full_name")
    rules = serializers.SerializerMethodField("get_rules")

    class Meta:
        model = UserModel
        fields = ("id", "sub", "username", "picurl", "full_name", "rules")

    def get_full_name(self, obj):
        return obj.user_profile.get_full_name()

    def get_rules(self, obj):
        return AdminStaffsListCreateUpdateSerializer(
            obj.user_admin.all(), many=True
        ).data


class AdminStaffsListCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminModel
        fields = ("id", "user", "role", "schools", "fields")
        extra_kwargs = {"user": {"write_only": True}}

    def create(self, validated_data):
        return AdminModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field_name in validated_data:
            setattr(instance, field_name, validated_data[field_name])
        instance.save()
        return instance
