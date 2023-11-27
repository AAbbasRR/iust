from rest_framework import status
from rest_framework.authtoken.models import Token

from app_occupation.tests import TestOccupationSetUp

from app_occupation.models import LatestOccupationModel
from app_occupation.api.serializers.latest_occupation import LatestOccupationSerializer
from app_user.models import UserModel

from utils import BaseErrors
from utils.data_list import occupation_options

from datetime import datetime


class UserLatestOccupationApiTestCase(TestOccupationSetUp):
    def setUp(self):
        super(UserLatestOccupationApiTestCase, self).setUp()

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

        self.occupation = [value[0] for value in occupation_options]

    def test_methods(self):
        self.create_latest_occupation_missing_fields()
        self.create_latest_occupation_invalid_occupation()
        self.retrieve_latest_occupation()
        self.update_latest_occupation()

    def create_latest_occupation_missing_fields(self):
        response = self.client.post(
            self.create_latest_occupation_api,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                "occupation": ["This field is required."],
                "organization": ["This field is required."],
                "from_date": ["This field is required."],
                "to_date": ["This field is required."],
            },
        )

    def create_latest_occupation_invalid_occupation(self):
        data = {
            "occupation": "invalid",
            "organization": self.fake_data.company(),
            "from_date": self.fake_data.date(),
            "to_date": self.fake_data.date(),
            "description": self.fake_data.text(),
        }
        response = self.client.post(
            self.create_latest_occupation_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                "occupation": ['"invalid" is not a valid choice.'],
            },
        )

    def retrieve_latest_occupation(self):
        response = self.client.get(
            self._detail_update_latest_occupation_api(self.application_obj.tracking_id),
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        latest_occupation = LatestOccupationModel.objects.get(
            application=self.application_obj
        )
        self.assertIsNotNone(latest_occupation)
        self.assertEqual(
            response_json,
            LatestOccupationSerializer(latest_occupation, many=False).data,
        )

    def update_latest_occupation(self):
        data = {
            "occupation": self.fake_data.random_choices(self.occupation, 1)[0],
            "organization": self.fake_data.company(),
        }
        response = self.client.put(
            self._detail_update_latest_occupation_api(self.application_obj.tracking_id),
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        try:
            latest_occupation = LatestOccupationModel.objects.get(
                application=self.application_obj
            )
            self.assertIsNotNone(latest_occupation)
            response_json = response.json()
            self.assertEqual(
                response_json,
                LatestOccupationSerializer(latest_occupation, many=False).data,
            )
            for key, value in data.items():
                self.assertEqual(getattr(latest_occupation, key), value)
        except LatestOccupationModel.DoesNotExist:
            self.assertTrue(False)
