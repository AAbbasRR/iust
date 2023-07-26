from django.contrib.auth import get_user_model

from rest_framework import serializers

from app_education.models import BachelorDegreeModel

UserModel = get_user_model()


class BachelorDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BachelorDegreeModel
        fields = (
            'id',
            'country',
            'city',
            'date_of_graduation',
            'gpa',
            'field_of_study',
            'university'
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'country': {'required': True},
            'city': {'required': True},
            'date_of_graduation': {'required': True},
            'gpa': {'required': True},
            'field_of_study': {'required': True},
            'university': {'required': True},
        }

    def __init__(self, *args, **kwargs):
        super(BachelorDegreeSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ['PUT', 'PATCH']:
                for field_name, field in self.fields.items():
                    field.required = False

    def update(self, instance, validated_data):
        for field_name in validated_data:  # update bachelor degree fields
            setattr(instance, field_name, validated_data[field_name])
        instance.save()
        return instance
