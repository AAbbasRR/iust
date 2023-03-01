from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions

from app_occupation.models import LatestOccupationModel
from app_application.models import ApplicationModel

from utils import BaseErrors

UserModel = get_user_model()


class LatestOccupationSerializer(serializers.ModelSerializer):
    tracking_id = serializers.CharField(
        max_length=12,
        required=True,
        write_only=True
    )

    class Meta:
        model = LatestOccupationModel
        fields = (
            'id',
            'tracking_id',
            'occupation',
            'organization',
            'from_date',
            'to_date',
            'description',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'occupation': {'required': True},
            'organization': {'required': True},
            'from_date': {'required': True},
            'to_date': {'required': True},
            'description': {'required': False},
        }

    def __init__(self, *args, **kwargs):
        super(LatestOccupationSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ['PUT', 'PATCH']:
                for field_name, field in self.fields.items():
                    field.required = False

    def validate_tracking_id(self, value):
        application_obj = ApplicationModel.objects.find_with_tracking_id(value)
        if application_obj is not None:
            return application_obj
        else:
            raise exceptions.NotFound(BaseErrors.tracking_id_not_found)

    def create(self, validated_data):
        application_obj = validated_data.pop('tracking_id')
        latest_occupation_obj = LatestOccupationModel.objects.create(
            application=application_obj,
            **validated_data
        )
        return latest_occupation_obj

    def update(self, instance, validated_data):
        try:
            validated_data.pop('tracking_id')
        except KeyError:
            pass
        for field_name in validated_data:  # update latest occupation fields
            setattr(instance, field_name, validated_data[field_name])
        instance.save()
        return instance
