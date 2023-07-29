from django.contrib.auth import get_user_model

from rest_framework import serializers

from app_application.models import ApplicationModel

UserModel = get_user_model()


class ApplicationSerializer(serializers.ModelSerializer):
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
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'tracking_id': {'read_only': True},
            'full_name': {'required': True},
            'comments': {'required': False},
            'applied_program': {'required': True},
            'financial_self_support': {'required': True},
            'degree': {'required': True},
            'faculty': {'required': True},
            'field_of_study': {'required': True},
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

    def create(self, validated_data):
        application_obj = ApplicationModel.objects.create(
            user=self.user,
            **validated_data
        )
        return application_obj

    def update(self, instance, validated_data):
        for field_name in validated_data:  # update application fields
            setattr(instance, field_name, validated_data[field_name])
        instance.save()
        return instance
