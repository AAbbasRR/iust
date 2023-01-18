from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions

from utils import RedisKeys, Redis, BaseErrors, ManageMailService

User = get_user_model()


class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(ForgetPasswordSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate_email(self, value):
        user_obj = User.objects.find_by_email(value)
        if user_obj is None:
            raise exceptions.NotFound(BaseErrors.user_not_found)
        self.user = user_obj
        return value

    def validate(self, attrs):
        redis_management = Redis(self.user.email, f'{RedisKeys.forget_password}_otp_code')
        if redis_management.exists():
            raise exceptions.ParseError({
                'message': BaseErrors.otp_code_has_already_been_sent,
                'time': redis_management.get_expire()
            })
        else:
            manage_email_obj = ManageMailService(self.user.email)
            manage_email_obj.send_otp_code(RedisKeys.forget_password)
            return True


class ValidateForgetPasswordOTPSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
    )
    otp_code = serializers.IntegerField(
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(UserVerifyRegisterSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate_email(self, value):
        user_obj = User.objects.find_by_email(value)
        if user_obj is None:
            raise exceptions.NotFound(BaseErrors.user_not_found)
        self.user = user_obj
        return value

    def validate(self, attrs):
        redis_management = Redis(self.user.email, f'{RedisKeys.activate_account}_otp_code')
        result_check_validate = redis_management.validate(attrs['otp_code'])
        if result_check_validate is None:
            raise exceptions.ParseError(BaseErrors.otp_code_expired)
        else:
            if result_check_validate is False:
                raise exceptions.ParseError(BaseErrors.invalid_otp_code)
            else:
                redis_management.delete()
                self.user.activate()
                return True
