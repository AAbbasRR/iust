from django.contrib.auth import get_user_model

from rest_framework import status

from app_user.tests import TestUserSetUp

from utils import Redis, RedisKeys, BaseErrors

User = get_user_model()


class UserRegisterApiTestCase(TestUserSetUp):
    def setUp(self):
        super(UserRegisterApiTestCase, self).setUp()

        self.invalid_email_address = {
            "email": "mailmail.com",
            "password": "a1A23456",
            "re_password": "a1A23456",
            "otp_code": "12345"
        }

        self.invalid_password = {
            "email": "mail@mail.com",
            "password": "123456",
            "re_password": "123456",
            "otp_code": "12345"
        }

        self.invalid_passwords_match = {
            "email": "mail@mail.com",
            "password": "a1A23456",
            "re_password": "123456",
            "otp_code": "12345"
        }

        self.success_register = {
            "email": "mail@mail.com",
            "password": "a1A23456",
            "re_password": "a1A23456",
            "otp_code": "12345"
        }

        self.not_found_account = {
            "email": "notfound@mail.com",
            "password": "a1A23456",
            "re_password": "a1A23456",
            "otp_code": "12345"
        }

        self.user_not_activated = {
            "email": "mail2@mail.com",
            "password": "a1A23456",
            "re_password": "a1A23456",
            "otp_code": "12345"
        }
        self.user2_obj = User.objects.register_user(
            email=self.user_not_activated['email'],
            password=self.user_not_activated['password']
        )
        redis_management = Redis(self.user2_obj.email, f'{RedisKeys.activate_account}_otp_code')
        redis_management.delete()

    def test_methods(self):
        self.register_api_test()
        self.active_account_api_test()
        self.resend_activation_code_api_test()

    def register_api_test(self):
        # check method error
        response = self.client.get(self.register_api)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        # check required Field
        response = self.client.post(self.register_api)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue('email' in response_keys)
        self.assertTrue('password' in response_keys)
        self.assertTrue('re_password' in response_keys)

        # check invalid email address
        response = self.client.post(self.register_api, self.invalid_email_address)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue('email' in response_keys)
        self.assertTrue('password' not in response_keys)

        # check password validator
        response = self.client.post(self.register_api, self.invalid_password)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue('password' in response_keys)
        self.assertTrue('email' not in response_keys)

        # check match password and re_password validator
        response = self.client.post(self.register_api, self.invalid_passwords_match)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue('detail' in response_keys)

        # success register
        response = self.client.post(self.register_api, self.success_register)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_json = response.json()
        self.assertEqual(response_json['email'], self.success_register['email'])
        redis_management = Redis(response_json['email'], f'{RedisKeys.activate_account}_otp_code')
        self.otp_code = redis_management.get_value()

        # user existed error
        response = self.client.post(self.register_api, self.success_register)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue('email' in response_keys)

    def active_account_api_test(self):
        # check method error
        response = self.client.get(self.active_account_api)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        # check required Field
        response = self.client.post(self.active_account_api)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue('email' in response_keys)
        self.assertTrue('otp_code' in response_keys)

        # check invalid email address
        response = self.client.post(self.active_account_api, self.invalid_email_address)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue('email' in response_keys)

        # check email not found
        response = self.client.post(self.active_account_api, self.not_found_account)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue('detail' in response_keys)

        # invalid otp_code value
        response = self.client.post(self.active_account_api, self.success_register)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(response_json['detail'], BaseErrors.invalid_otp_code)
        self.assertNotEqual(self.success_register['otp_code'], self.otp_code)

        # expire otp_code key
        redis_management = Redis(self.success_register['email'], f'{RedisKeys.activate_account}_otp_code')
        redis_management.delete()
        self.assertFalse(redis_management.exists())
        self.assertLessEqual(redis_management.get_expire(), -1)
        response = self.client.post(self.active_account_api, self.success_register)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(response_json['detail'], BaseErrors.otp_code_expired)
        self.assertNotEqual(self.success_register['otp_code'], self.otp_code)

        # success active account
        redis_management = Redis(self.success_register['email'], f'{RedisKeys.activate_account}_otp_code')
        redis_management.set_value(self.otp_code)
        response = self.client.post(self.active_account_api, {
            "email": self.success_register['email'],
            "otp_code": self.otp_code
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.success_user_obj = User.objects.find_by_email(self.success_register['email'])
        self.assertTrue(self.success_user_obj.is_active)
        self.assertFalse(redis_management.exists())

    def resend_activation_code_api_test(self):
        # check method error
        response = self.client.get(self.resend_activation_otp_api)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        # check required Field
        response = self.client.post(self.resend_activation_otp_api)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue('email' in response_keys)

        # check invalid email address
        response = self.client.post(self.resend_activation_otp_api, self.invalid_email_address)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue('email' in response_keys)

        # check email not found
        response = self.client.post(self.resend_activation_otp_api, self.not_found_account)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue('detail' in response_keys)

        # user is active
        response = self.client.post(self.resend_activation_otp_api, self.success_register)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(response_json['detail'], BaseErrors.user_account_is_active)
        self.assertTrue(self.success_user_obj.is_active)

        # success otp_code sent
        response = self.client.post(self.resend_activation_otp_api, self.user_not_activated)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        redis_management = Redis(self.user_not_activated['email'], f'{RedisKeys.activate_account}_otp_code')
        self.assertTrue(redis_management.exists())
        try:
            self.assertEqual(type(int(redis_management.get_value())), int().__class__)
            self.assertLessEqual(0, redis_management.get_expire())
        except TypeError:
            self.assertTrue(False)

        # otp_code has already been sent
        response = self.client.post(self.resend_activation_otp_api, self.user_not_activated)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(response_json['message'], BaseErrors.otp_code_has_already_been_sent)
