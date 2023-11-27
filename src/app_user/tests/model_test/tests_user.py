from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from rest_framework.authtoken.models import Token

from app_user.tests import TestUserSetUp

from utils import BaseErrors, RedisKeys, Redis

UserModel = get_user_model()


class UserTestCase(TestUserSetUp):
    def setUp(self):
        super(UserTestCase, self).setUp()

        self.user_model_data = {
            "success": {
                "email": "mail@mail.com",
                "password": "123456",
                "new_password": "1234567",
            },
            "not_found": {"email": "notmail@mail.com", "password": "123456"},
        }

    def test_methods(self):
        self.empty_token_model_test()
        self.method_register_user_test()
        self.unique_user_email_test()
        self.method_find_by_email_test()
        self.method_activate_test()
        self.method_change_password_test()

    def empty_token_model_test(self):
        tokens = Token.objects.all()
        self.assertEqual(tokens.count(), 0)
        users = UserModel.objects.all()
        self.assertEqual(users.count(), 0)

    def method_register_user_test(self):
        error = False
        try:
            user_obj = UserModel.objects.register_user()
            error = False
        except ValueError as error_msg:
            error = True
            self.assertEqual(str(error_msg), BaseErrors.user_must_have_email)
        self.assertTrue(error)
        try:
            user_obj = UserModel.objects.register_user(
                email=self.user_model_data["success"]["email"]
            )
            error = False
        except ValueError as error_msg:
            error = True
            self.assertEqual(str(error_msg), BaseErrors.user_must_have_password)
        self.assertTrue(error)
        try:
            user_obj = UserModel.objects.register_user(
                email=self.user_model_data["success"]["email"],
                password=self.user_model_data["success"]["password"],
            )
            error = False
        except ValueError as error_msg:
            error = True
        self.assertFalse(error)

        self.assertEqual(user_obj.email, self.user_model_data["success"]["email"])
        self.assertTrue(
            user_obj.check_password(self.user_model_data["success"]["password"])
        )
        self.assertFalse(user_obj.is_active)
        self.assertFalse(user_obj.is_staff)
        self.assertFalse(user_obj.is_superuser)
        tokens = Token.objects.all()
        self.assertEqual(tokens.count(), 1)
        users = UserModel.objects.all()
        self.assertEqual(users.count(), 1)

        redis_management = Redis(
            user_obj.email, f"{RedisKeys.activate_account}_otp_code"
        )
        self.assertTrue(redis_management.exists())
        try:
            self.assertEqual(type(int(redis_management.get_value())), int().__class__)
            self.assertLessEqual(0, redis_management.get_expire())
        except TypeError:
            self.assertTrue(False)

    def unique_user_email_test(self):
        error = False
        try:
            UserModel.objects.register_user(
                email=self.user_model_data["success"]["email"],
                password=self.user_model_data["success"]["password"],
            )
            error = False
        except IntegrityError:
            error = True
        self.assertTrue(error)

    def method_find_by_email_test(self):
        error = False
        try:
            user_obj = UserModel.objects.find_by_email()
            error = False
        except ValueError as error_msg:
            error = True
            self.assertEqual(str(error_msg), BaseErrors.user_must_have_email)
        self.assertTrue(error)
        user_obj = UserModel.objects.find_by_email(
            email=self.user_model_data["not_found"]["email"]
        )
        self.assertIsNone(user_obj)
        user_obj = UserModel.objects.find_by_email(
            email=self.user_model_data["success"]["email"]
        )
        self.assertIsNotNone(user_obj)
        self.assertEqual(user_obj.email, self.user_model_data["success"]["email"])
        self.assertTrue(
            user_obj.check_password(self.user_model_data["success"]["password"])
        )

    def method_activate_test(self):
        user_obj = UserModel.objects.find_by_email(
            email=self.user_model_data["success"]["email"]
        )
        self.assertFalse(user_obj.is_active)
        user_obj.activate()
        self.assertTrue(user_obj.is_active)
        self.assertFalse(user_obj.is_staff)
        self.assertFalse(user_obj.is_superuser)
        self.assertTrue(
            user_obj.check_password(self.user_model_data["success"]["password"])
        )

    def method_change_password_test(self):
        user_obj = UserModel.objects.find_by_email(
            email=self.user_model_data["success"]["email"]
        )
        user_obj.change_password(self.user_model_data["success"]["new_password"])
        self.assertFalse(
            user_obj.check_password(self.user_model_data["success"]["password"])
        )
        self.assertTrue(
            user_obj.check_password(self.user_model_data["success"]["new_password"])
        )
        self.assertTrue(user_obj.is_active)
        self.assertFalse(user_obj.is_staff)
        self.assertFalse(user_obj.is_superuser)
