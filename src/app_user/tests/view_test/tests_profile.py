from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.authtoken.models import Token

from app_user.tests import TestUserSetUp

from app_user.models import ProfileModel
from app_user.api.serializers.profile import ProfileSerializer

from utils.data_list import gender_options, language_status_options

UserModel = get_user_model()


class UserProfileApiTestCase(TestUserSetUp):
    def setUp(self):
        super(UserProfileApiTestCase, self).setUp()

        self.success_profile = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }
        self.user_obj = UserModel.objects.register_user(
            email=self.success_profile["email"],
            password=self.success_profile["password"],
        )
        self.user_obj.activate()
        self.user_token = Token.objects.get(user=self.user_obj)

        gender = [value[0] for value in gender_options]
        languages = [value[0] for value in language_status_options]

        self.profile_data = {
            "first_name": self.fake_data.first_name(),
            "last_name": self.fake_data.last_name(),
            "birth_date": self.fake_data.date_of_birth(),
            "gender": self.fake_data.random_choices(gender, 1)[0],
            "phone_number": self.fake_data.phone_number(),
            "nationality": self.fake_data.country(),
            "mother_language": self.fake_data.language_name(),
            "other_languages": "FR, ES",
            "english_status": self.fake_data.random_choices(languages, 1)[0],
            "persian_status": self.fake_data.random_choices(languages, 1)[0],
        }
        self.updated_profile_data = {
            "first_name": self.fake_data.first_name(),
            "last_name": self.fake_data.last_name(),
            "mother_language": self.fake_data.language_name(),
            "english_status": self.fake_data.random_choices(languages, 1)[0],
        }

    def test_methods(self):
        self.create_profile_missing_fields()
        self.create_profile_invalid_choices()
        self.create_profile()
        self.retrieve_profile()
        self.update_profile()

    def create_profile_missing_fields(self):
        response = self.client.post(
            self.create_profile_api, HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                "first_name": ["This field is required."],
                "last_name": ["This field is required."],
                "birth_date": ["This field is required."],
                "gender": ["This field is required."],
                "nationality": ["This field is required."],
                "mother_language": ["This field is required."],
                "english_status": ["This field is required."],
                "persian_status": ["This field is required."],
            },
        )

    def create_profile_invalid_choices(self):
        data = {
            "first_name": "Test",
            "last_name": "User",
            "birth_date": "1990-01-01",
            "gender": "invalid",
            "nationality": "US",
            "mother_language": "EN",
            "other_languages": "",
            "english_status": "invalid",
            "persian_status": "invalid",
        }
        response = self.client.post(
            self.create_profile_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                "gender": ['"invalid" is not a valid choice.'],
                "english_status": ['"invalid" is not a valid choice.'],
                "persian_status": ['"invalid" is not a valid choice.'],
            },
        )

    def create_profile(self):
        response = self.client.post(
            self.create_profile_api,
            self.profile_data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProfileModel.objects.count(), 1)
        try:
            profile = ProfileModel.objects.get(user=self.user_obj)
            self.assertIsNotNone(profile)
            response_json = response.json()
            self.assertEqual(response_json, ProfileSerializer(profile, many=False).data)
            for key, value in self.profile_data.items():
                self.assertEqual(getattr(profile, key), value)
        except ProfileModel.DoesNotExist:
            self.assertTrue(False)

    def retrieve_profile(self):
        response = self.client.get(
            self.detail_update_profile_api,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        profile = ProfileModel.objects.get(user=self.user_obj)
        self.assertIsNotNone(profile)
        self.assertEqual(response_json, ProfileSerializer(profile, many=False).data)

    def update_profile(self):
        response = self.client.put(
            self.detail_update_profile_api,
            self.updated_profile_data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        try:
            profile = ProfileModel.objects.get(user=self.user_obj)
            self.assertIsNotNone(profile)
            response_json = response.json()
            self.assertEqual(response_json, ProfileSerializer(profile, many=False).data)
            for key, value in self.updated_profile_data.items():
                self.assertEqual(getattr(profile, key), value)
        except ProfileModel.DoesNotExist:
            self.assertTrue(False)
