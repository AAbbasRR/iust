from rest_framework import serializers

from app_occupation.models import LatestOccupationModel


class LatestOccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestOccupationModel
        fields = (
            'id',
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

    def update(self, instance, validated_data):
        for field_name in validated_data:  # update latest occupation fields
            setattr(instance, field_name, validated_data[field_name])
        instance.save()
        return instance
