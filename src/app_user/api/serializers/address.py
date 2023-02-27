from django.contrib.auth import get_user_model

from rest_framework import serializers

from app_user.models import AddressModel

UserModel = get_user_model()


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = (
            'id',
            'country',
            'city',
            'country_code',
            'postal_code',
            'city_code',
            'phone_number',
            'address',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'country': {'required': True},
            'city': {'required': True},
            'country_code': {'required': False},
            'postal_code': {'required': True},
            'city_code': {'required': False},
            'phone_number': {'required': False},
            'address': {'required': True},
        }

    def __init__(self, *args, **kwargs):
        super(AddressSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ['PUT', 'PATCH']:
                for field_name, field in self.fields.items():
                    field.required = False

    def create(self, validated_data):
        address_obj = AddressModel.objects.create(
            user=self.user,
            **validated_data
        )
        return address_obj

    def update(self, instance, validated_data):
        for field_name in validated_data:  # update address fields
            setattr(instance, field_name, validated_data[field_name])
        instance.save()
        return instance
