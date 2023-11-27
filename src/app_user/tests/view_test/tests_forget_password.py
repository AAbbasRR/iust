from django.contrib.auth import get_user_model

from rest_framework import status

from app_user.tests import TestUserSetUp

from utils import Redis, RedisKeys, BaseErrors

UserModel = get_user_model()


class UserForgetPasswordApiTestCase(TestUserSetUp):
    def setUp(self):
        super(UserForgetPasswordApiTestCase, self).setUp()

        self.invalid_email_address = {
            "email": "mailmail.com",
            "password": "a1A23456",
            "re_password": "a1A23456",
            "otp_code": "12345",
        }

        self.invalid_password = {
            "email": "mail@mail.com",
            "password": "123456",
            "re_password": "123456",
            "otp_code": "12345",
        }

        self.invalid_passwords_match = {
            "email": "mail@mail.com",
            "password": "a1A23456",
            "re_password": "123456",
            "otp_code": "12345",
        }

        self.not_found_account = {
            "email": "notfound@mail.com",
            "password": "a1A23456",
            "re_password": "a1A23456",
            "otp_code": "12345",
        }

        self.success_forget_password = {
            "email": "mail@mail.com",
            "old_password": "a1A234567",
            "password": "a1A23456@",
            "re_password": "a1A23456@",
            "otp_code": "12345",
        }
        user_obj = UserModel.objects.register_user(
            email=self.success_forget_password["email"],
            password=self.success_forget_password["old_password"],
        )
        user_obj.activate()
        redis_management = Redis(
            user_obj.email, f"{RedisKeys.activate_account}_otp_code"
        )
        redis_management.delete()

    def test_methods(self):
        self.forget_password_api_test()
        self.validate_forget_password_api_test()
        self.complete_forget_password_api_test()

    def forget_password_api_test(self):
        # check required Field
        response = self.client.post(self.forget_password_api)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue("email" in response_keys)

        # check invalid email address
        response = self.client.post(
            self.forget_password_api, self.invalid_email_address
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue("email" in response_keys)

        # check email not found
        response = self.client.post(self.forget_password_api, self.not_found_account)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue("detail" in response_keys)

        # success forget password account
        response = self.client.post(
            self.forget_password_api, self.success_forget_password
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        redis_management = Redis(
            self.success_forget_password["email"],
            f"{RedisKeys.forget_password}_otp_code",
        )
        self.otp_code = redis_management.get_value()
        self.assertTrue(redis_management.exists())
        try:
            self.assertEqual(type(int(redis_management.get_value())), int().__class__)
            self.assertLessEqual(0, redis_management.get_expire())
        except TypeError:
            self.assertTrue(False)

        # otp_code has already been sent
        response = self.client.post(
            self.forget_password_api, self.success_forget_password
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json["message"], BaseErrors.otp_code_has_already_been_sent
        )

    def validate_forget_password_api_test(self):
        # check required Field
        response = self.client.post(self.validate_forget_password_api)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue("email" in response_keys)
        self.assertTrue("otp_code" in response_keys)

        # check invalid email address
        response = self.client.post(
            self.validate_forget_password_api, self.invalid_email_address
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue("email" in response_keys)

        # check email not found
        response = self.client.post(
            self.validate_forget_password_api, self.not_found_account
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue("detail" in response_keys)

        # invalid otp_code value
        response = self.client.post(
            self.validate_forget_password_api, self.success_forget_password
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(response_json["detail"], BaseErrors.invalid_otp_code)
        self.assertNotEqual(self.success_forget_password["otp_code"], self.otp_code)

        # expire otp_code key
        redis_management = Redis(
            self.success_forget_password["email"],
            f"{RedisKeys.forget_password}_otp_code",
        )
        redis_management.delete()
        self.assertFalse(redis_management.exists())
        self.assertLessEqual(redis_management.get_expire(), -1)
        response = self.client.post(
            self.validate_forget_password_api, self.success_forget_password
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(response_json["detail"], BaseErrors.otp_code_expired)
        self.assertNotEqual(self.success_forget_password["otp_code"], self.otp_code)

        # success validated otp_code forget password
        redis_management = Redis(
            self.success_forget_password["email"],
            f"{RedisKeys.forget_password}_otp_code",
        )
        redis_management.set_value(self.otp_code)
        response = self.client.post(
            self.validate_forget_password_api,
            {"email": self.success_forget_password["email"], "otp_code": self.otp_code},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(redis_management.exists())
        redis_management = Redis(
            self.success_forget_password["email"], RedisKeys.forget_password
        )
        self.assertTrue(redis_management.exists())
        self.assertTrue(redis_management.get_status_value())
        self.assertLessEqual(0, redis_management.get_expire())

    def complete_forget_password_api_test(self):
        # check required Field
        response = self.client.post(self.complete_forget_password_api)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue("email" in response_keys)
        self.assertTrue("password" in response_keys)
        self.assertTrue("re_password" in response_keys)

        # check invalid email address
        response = self.client.post(
            self.complete_forget_password_api, self.invalid_email_address
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue("email" in response_keys)
        self.assertTrue("password" not in response_keys)

        # check email not found
        response = self.client.post(
            self.complete_forget_password_api, self.not_found_account
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue("detail" in response_keys)

        # check password validator
        response = self.client.post(
            self.complete_forget_password_api, self.invalid_password
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue("password" in response_keys)
        self.assertTrue("email" not in response_keys)

        # check match password and re_password validator
        response = self.client.post(
            self.complete_forget_password_api, self.invalid_passwords_match
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        response_keys = list(response_json.keys())
        self.assertTrue("detail" in response_keys)

        # success complete forget password
        response = self.client.post(
            self.complete_forget_password_api, self.success_forget_password
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        redis_management = Redis(
            self.success_forget_password["email"], RedisKeys.forget_password
        )
        self.assertFalse(redis_management.exists())
        self.assertLessEqual(redis_management.get_expire(), -1)
        user_obj = UserModel.objects.find_by_email(
            self.success_forget_password["email"]
        )
        self.assertFalse(
            user_obj.check_password(self.success_forget_password["old_password"])
        )
        self.assertTrue(
            user_obj.check_password(self.success_forget_password["password"])
        )

        # do not have access to change password
        response = self.client.post(
            self.complete_forget_password_api, self.success_forget_password
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json["detail"],
            BaseErrors.user_dont_have_forget_password_permission,
        )
        redis_management = Redis(
            self.success_forget_password["email"], RedisKeys.forget_password
        )
        self.assertFalse(redis_management.exists())
        self.assertLessEqual(redis_management.get_expire(), -1)
