from rest_framework import exceptions, serializers
from rest_framework.authtoken.models import Token

from app_user.models import UserModel

from utils.base_errors import BaseErrors

import requests


class AdminOauthLoginSerializer(serializers.Serializer):
    access_token = serializers.CharField(
        max_length=64,
        required=True,
    )

    def validate(self, attrs):
        response = requests.get("https://its.iust.ac.ir/oauth2/token", auth=f"Bearer {attrs['access_token']}")
        if response.status_code == 200:
            print(response)
            # user_obj = UserModel.objects.find_admin_by_email(email=attrs['email'])
            # if user_obj is None or user_obj.check_password(attrs['password']) is False:
            #     raise exceptions.ParseError(BaseErrors.invalid_email_or_password)
            # else:
            #     user_obj.set_last_login()
            #     user_token = Token.objects.get(user=user_obj)
            #     return {
            #         "id": user_obj.id,
            #         "email": user_obj.email,
            #         "auth_token": user_token.key
            #     }
        else:
            raise exceptions.ParseError(BaseErrors.invalid_access_token)
