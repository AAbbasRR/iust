from django.contrib.auth import get_user_model

from rest_framework import serializers

from app_application.models import ApplicationModel
from app_user.api.serializers.profile import ProfileSerializer
from app_user.api.serializers.address import AddressSerializer

UserModel = get_user_model()


class ApplicationSerializer(serializers.ModelSerializer):
    user_detail = serializers.SerializerMethodField("get_user_detail")

    class Meta:
        model = ApplicationModel
        fields = (
            "id",
            "tracking_id",
            "full_name",
            "comments",
            "applied_program",
            "financial_self_support",
            "degree",
            "faculty",
            "field_of_study",
            "status",
            "created_at",
            "user_detail",
            "step",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "tracking_id": {"read_only": True},
            "full_name": {"required": False},
            "comments": {"required": False},
            "applied_program": {"required": False},
            "financial_self_support": {"required": False},
            "degree": {"required": False},
            "faculty": {"required": False},
            "field_of_study": {"required": False},
            "status": {"read_only": True},
            "created_at": {"read_only": True},
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get("request")
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ["PUT", "PATCH"]:
                for field_name, field in self.fields.items():
                    field.required = False

    def get_user_detail(self, obj):
        return {
            "profile": ProfileSerializer(
                self.user.user_profile, many=False, read_only=True, context=self.context
            ).data,
            "address": AddressSerializer(
                self.user.user_address, many=False, read_only=True, context=self.context
            ).data,
        }

    def create(self, validated_data):
        application_obj = ApplicationModel.objects.create(
            user=self.user, **validated_data
        )
        have_document = False
        try:
            if application_obj.application_document is not None:
                have_document = True
        except:
            pass
        if (
            application_obj.degree is not None
            and application_obj.field_of_study is not None
            and application_obj.faculty is not None
            and application_obj.financial_self_support is not None
            and application_obj.applied_program is not None
            and application_obj.full_name is not None
            and have_document
        ):
            application_obj.status = ApplicationModel.ApplicationStatusOptions.Current
            application_obj.save()
        return application_obj

    def update(self, instance, validated_data):
        for field_name in validated_data:  # update application fields
            setattr(instance, field_name, validated_data[field_name])
        have_document = False
        try:
            if instance.application_document is not None:
                have_document = True
        except:
            pass
        if (
            instance.degree is not None
            and instance.field_of_study is not None
            and instance.faculty is not None
            and instance.financial_self_support is not None
            and instance.applied_program is not None
            and instance.full_name is not None
            and have_document
        ):
            instance.status = ApplicationModel.ApplicationStatusOptions.Current
        instance.save()
        return instance
