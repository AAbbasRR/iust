from django.contrib.auth.password_validation import validate_password

from rest_framework import (
    serializers,
    exceptions
)

from app_user.models import UserModel

from utils.base_errors import BaseErrors


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        required=True,
        write_only=True,
    )
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
    )
    new_re_password = serializers.CharField(
        required=True,
        write_only=True,
    )

    class Meta:
        model = UserModel
        fields = (
            "old_password",
            "new_password",
            "new_re_password",
        )

    def __init__(self, *args, **kwargs):
        super(ChangePasswordSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user

    def validate_old_password(self, value):
        if not self.user.check_password(value):
            raise serializers.ValidationError(BaseErrors.old_password_is_incorrect)
        return value

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_re_password']:
            raise exceptions.ParseError({
                "new_password": [BaseErrors.passwords_did_not_match],
                "new_re_password": [BaseErrors.passwords_did_not_match],
            })
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
