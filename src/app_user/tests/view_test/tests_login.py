from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.authtoken.models import Token

from app_user.tests import TestUserSetUp

from utils import Redis, RedisKeys, BaseErrors

User = get_user_model()


class UserLoginApiTestCase(TestUserSetUp):
    def setUp(self):
        super(UserLoginApiTestCase, self).setUp()

        self.invalid_email_address = {
            "email": "mailmail.com",
            "password": "a1A23456",
        }

        self.success_login = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }
        self.user_obj = User.objects.register_user(email=self.success_login['email'], password=self.success_login['password'])
        self.user_obj.activate()
        redis_management = Redis(self.user_obj.email, f'{RedisKeys.activate_account}_otp_code')
        redis_management.delete()

        self.not_found_account = {
            "email": "notfound@mail.com",
            "password": "a1A23456",
        }

        self.invalid_password = {
            "email": "mail@mail.com",
            "password": "123456",
        }

        self.user_not_activated = {
            "email": "mail2@mail.com",
            "password": "a1A23456",
        }
        self.user2_obj = User.objects.register_user(email=self.user_not_activated['email'], password=self.user_not_activated['password'])
        redis_management = Redis(self.user2_obj.email, f'{RedisKeys.activate_account}_otp_code')
        redis_management.delete()

    def test_methods(self):
        self.login_api_test()

    def login_api_test(self):
        # check method error
        response = self.client.get(self.login_api)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        # check required Field
        response = self.client.post(self.login_api)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue('email' in response_keys)
        self.assertTrue('password' in response_keys)

        # check invalid email address
        response = self.client.post(self.login_api, self.invalid_email_address)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue('email' in response_keys)

        # check email or password is invalid
        response = self.client.post(self.login_api, self.not_found_account)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(response_json['detail'], BaseErrors.invalid_email_or_password)

        response = self.client.post(self.login_api, self.invalid_password)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(response_json['detail'], BaseErrors.invalid_email_or_password)

        # user account not activated
        response = self.client.post(self.login_api, self.user_not_activated)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(response_json['detail'], BaseErrors.user_account_not_active)
        self.assertFalse(self.user2_obj.is_active)
        redis_management = Redis(self.user2_obj.email, f'{RedisKeys.activate_account}_otp_code')
        self.assertTrue(redis_management.exists())
        try:
            self.assertEqual(type(int(redis_management.get_value())), int().__class__)
            self.assertLessEqual(0, redis_management.get_expire())
        except TypeError:
            self.assertTrue(False)

        # success login
        response = self.client.post(self.login_api, self.success_login)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        self.assertEqual(response_json['email'], self.user_obj.email)
        self.assertEqual(response_json['id'], self.user_obj.pk)
        self.assertTrue(self.user_obj.is_active)
        token = Token.objects.get(user=self.user_obj)
        self.assertEqual(response_json['auth_token'], token.key)
        redis_management = Redis(self.user_obj.email, f'{RedisKeys.activate_account}_otp_code')
        self.assertFalse(redis_management.exists())
