from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions

from app_education.models import ProgramRequestedModel
from app_application.models import ApplicationModel

from utils import BaseErrors
from utils.data_list import program_requested_data

UserModel = get_user_model()


class ProgramRequestedSerializer(serializers.ModelSerializer):
    tracking_id = serializers.CharField(
        max_length=12,
        required=True,
        write_only=True
    )

    class Meta:
        model = ProgramRequestedModel
        fields = (
            'id',
            'tracking_id',
            'degree',
            'faculty',
            'field_of_study',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'degree': {'required': True},
            'faculty': {'required': True},
            'field_of_study': {'required': True},
        }

    def __init__(self, *args, **kwargs):
        super(ProgramRequestedSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ['PUT', 'PATCH']:
                self.fields['tracking_id'].read_only = True
                for field_name, field in self.fields.items():
                    field.required = False

    def validate_tracking_id(self, value):
        application_obj = ApplicationModel.objects.find_with_tracking_id(value)
        if application_obj is not None:
            return application_obj
        else:
            raise exceptions.NotFound(BaseErrors.tracking_id_not_found)

    def validate(self, attrs):
        find_faculty = list(filter(lambda value: value[0] == attrs['faculty'], program_requested_data[attrs['degree']]['items']))
        if find_faculty:
            find_field_of_study = list(filter(lambda value: value[0] == attrs['field_of_study'], program_requested_data[attrs['degree']]['data'][attrs['faculty']]))
            if find_field_of_study:
                return attrs
            else:
                raise exceptions.ValidationError({
                    "field_of_study": BaseErrors._change_error_variable('invalid_choice_value', input=attrs['field_of_study'])
                })
        else:
            raise exceptions.ValidationError({
                "faculty": BaseErrors._change_error_variable('invalid_choice_value', input=attrs['faculty'])
            })

    def create(self, validated_data):
        application_obj = validated_data.pop('tracking_id')
        program_requested_obj = ProgramRequestedModel.objects.create(
            application=application_obj,
            **validated_data
        )
        return program_requested_obj

    def update(self, instance, validated_data):
        try:
            validated_data.pop('tracking_id')
        except KeyError:
            pass
        for field_name in validated_data:  # update program requested fields
            setattr(instance, field_name, validated_data[field_name])
        instance.save()
        return instance
