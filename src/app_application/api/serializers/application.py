from django.contrib.auth import get_user_model

from rest_framework import serializers

from app_application.models import ApplicationModel
from app_user.api.serializers.profile import ProfileSerializer
from app_user.api.serializers.address import AddressSerializer

UserModel = get_user_model()


class ApplicationSerializer(serializers.ModelSerializer):
    user_detail = serializers.SerializerMethodField(
        'get_user_detail'
    )

    class Meta:
        model = ApplicationModel
        fields = (
            'id',
            'tracking_id',
            'full_name',
            'comments',
            'applied_program',
            'financial_self_support',
            'degree',
            'faculty',
            'field_of_study',
            'university_status',
            'faculty_status',
            'created_at',

            'user_detail',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'tracking_id': {'read_only': True},
            'full_name': {'required': False},
            'comments': {'required': False},
            'applied_program': {'required': False},
            'financial_self_support': {'required': False},
            'degree': {'required': False},
            'faculty': {'required': False},
            'field_of_study': {'required': False},
            'university_status': {'read_only': True},
            'faculty_status': {'read_only': True},
            'created_at': {'read_only': True},
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ['PUT', 'PATCH']:
                for field_name, field in self.fields.items():
                    field.required = False

    def get_user_detail(self, obj):
        return {
            "profile": ProfileSerializer(self.user.user_profile, many=False, read_only=True, context=self.context).data,
            "address": AddressSerializer(self.user.user_address, many=False, read_only=True, context=self.context).data,
        }

    def create(self, validated_data):
        application_obj = ApplicationModel.objects.create(
            user=self.user,
            **validated_data
        )
        if application_obj.degree != None and application_obj.field_of_study != None and application_obj.faculty != None and application_obj.financial_self_support != None and application_obj.applied_program != None and application_obj.full_name != None:
            application_obj.university_status = "CRNT"
            application_obj.faculty_status = "CRNT"
            application_obj.save()
        return application_obj

    def update(self, instance, validated_data):
        for field_name in validated_data:  # update application fields
            setattr(instance, field_name, validated_data[field_name])
        if instance.degree != None and instance.field_of_study != None and instance.faculty != None and instance.financial_self_support != None and instance.applied_program != None and instance.full_name != None:
            instance.university_status = "CRNT"
            instance.faculty_status = "CRNT"
        instance.save()
        return instance
