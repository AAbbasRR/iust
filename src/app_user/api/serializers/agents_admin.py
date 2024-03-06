from rest_framework import serializers

from app_user.models import UserModel


class AdminAgentsListSerializers(serializers.ModelSerializer):
    count_applications = serializers.SerializerMethodField(
        "get_count_applications", read_only=True
    )

    class Meta:
        model = UserModel
        fields = ("id", "email", "jalali_date_joined", "count_applications", "locked")
        extra_kwargs = {
            "email": {"read_only": True},
            "jalali_date_joined": {"read_only": True},
        }

    def get_count_applications(self, obj):
        return obj.agent_applications.count()

    def update(self, instance, validated_data):
        for field_name in validated_data:  # update agent fields
            setattr(instance, field_name, validated_data[field_name])
        instance.save()
        return instance
