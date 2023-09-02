from django.contrib.auth import get_user_model

from app_user.models import ProfileModel
from app_user.tests import TestUserSetUp

UserModel = get_user_model()


class ProfileTestCase(TestUserSetUp):
    def setUp(self):
        super(ProfileTestCase, self).setUp()

        self.success_user = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }

        self.user_obj = UserModel.objects.register_user(
            email=self.success_user['email'],
            password=self.success_user['password']
        )
        self.user_obj.activate()

    def test_methods(self):
        self.create_test()
        self.delete_user_test()

    def create_test(self):
        profile_count = ProfileModel.objects.all().count()
        self.assertEqual(profile_count, 0)
        data = {
            "first_name": self.fake_data.first_name(),
            "last_name": self.fake_data.last_name(),
            "birth_date": self.fake_data.date_of_birth(),
            "gender": self.fake_data.random_choices(elements=['MAL', 'FML', 'OTR'], length=1)[0],
            "nationality": self.fake_data.country(),
            "phone_number": self.fake_data.phone_number(),
            "mother_language": self.fake_data.language_name(),
            "other_languages": self.fake_data.language_name(),
            "english_status": self.fake_data.random_choices(elements=['WEK', 'GOD', 'EXT'], length=1)[0],
            "persian_status": self.fake_data.random_choices(elements=['WEK', 'GOD', 'EXT'], length=1)[0],
        }
        self.success_profile_obj = ProfileModel.objects.create(
            user=self.user_obj,
            **data
        )
        self.assertIsNotNone(self.success_profile_obj)
        self.assertEqual(self.success_profile_obj.user.email, self.user_obj.email)
        self.assertEqual(self.success_profile_obj.first_name, data['first_name'])
        self.assertEqual(self.success_profile_obj.last_name, data['last_name'])
        self.assertEqual(self.success_profile_obj.gender, data['gender'])
        self.assertEqual(self.success_profile_obj.persian_status, data['persian_status'])
        profile_count = ProfileModel.objects.all().count()
        self.assertEqual(profile_count, 1)

    def delete_user_test(self):
        self.user_obj.delete()
        profile_count = ProfileModel.objects.all().count()
        self.assertEqual(profile_count, 0)
