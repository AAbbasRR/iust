from rest_framework import exceptions, serializers
from rest_framework.authtoken.models import Token

from app_user.models import UserModel

from utils.base_errors import BaseErrors

import requests
import json


class AdminOauthLoginSerializer(serializers.Serializer):
    access_token = serializers.CharField(
        max_length=64,
        required=True,
    )

    def validate(self, attrs):
        response = requests.get("https://its.iust.ac.ir/oauth2/userinfo",
                                headers={"Authorization": f"Bearer {attrs['access_token']}"})
        if response.status_code == 200:
            response_json = json.loads(response.content)
            user_obj, created = UserModel.objects.get_or_create(username=response_json["username"], is_superuser=True, is_active=True, is_staff=True)
            user_obj.sub = response_json["sub"]
            user_obj.picurl = response_json["picture"]
            try:
                user_obj.admin_role = getattr(UserModel.AdminOptions, response_json["usertype"])
            except AttributeError:
                pass
            user_obj.save()

            user_profile = user_obj.user_profile
            user_profile.first_name = response_json["firstname"]
            user_profile.last_name = response_json["lastname"]
            user_profile.save()

            user_obj.set_last_login()
            user_token = Token.objects.get(user=user_obj)
            return {
                "sub": user_obj.sub,
                "username": user_obj.username,
                "picurl": user_obj.picurl,
                "full_name": user_profile.get_full_name(),
                "auth_token": user_token.key
            }
        else:
            raise exceptions.ParseError(BaseErrors.invalid_access_token)
