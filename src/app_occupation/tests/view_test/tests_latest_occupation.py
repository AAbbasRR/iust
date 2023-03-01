from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.authtoken.models import Token

from app_occupation.tests import TestOccupationSetUp

from app_occupation.models import LatestOccupationModel
from app_occupation.api.serializers.latest_occupation import LatestOccupationSerializer
from app_application.models import ApplicationModel

from utils import BaseErrors
from utils.data_list import occupation_options

from datetime import datetime

UserModel = get_user_model()


class UserLatestOccupationApiTestCase(TestOccupationSetUp):

    def setUp(self):
        super(UserLatestOccupationApiTestCase, self).setUp()

        self.success_profile = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }
        self.user_obj = UserModel.objects.register_user(email=self.success_profile['email'], password=self.success_profile['password'])
        self.user_obj.activate()
        self.user_token = Token.objects.get(user=self.user_obj)

        self.application_obj = ApplicationModel.objects.create(
            user=self.user_obj
        )

        self.occupation = [value[0] for value in occupation_options]

    def test_methods(self):
        self.create_latest_occupation_missing_fields()
        self.create_invalid_tracking_id()
        self.create_latest_occupation_invalid_occupation()
        self.create_latest_occupation()
        self.retrieve_latest_occupation()
        self.update_latest_occupation()

    def create_latest_occupation_missing_fields(self):
        response = self.client.post(
            self.create_latest_occupation_api,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                'tracking_id': ['This field is required.'],
                'occupation': ['This field is required.'],
                'organization': ['This field is required.'],
                'from_date': ['This field is required.'],
                'to_date': ['This field is required.'],
            }
        )

    def create_invalid_tracking_id(self):
        data = {
            'tracking_id': "invalid_id",
            'occupation': self.fake_data.random_choices(self.occupation, 1)[0],
            'organization': self.fake_data.company(),
            'from_date': self.fake_data.date(),
            'to_date': self.fake_data.date(),
            'description': self.fake_data.text(),
        }
        response = self.client.post(
            self.create_latest_occupation_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_json = response.json()
        self.assertEqual(response_json, {
            'detail': BaseErrors.tracking_id_not_found
        })

    def create_latest_occupation_invalid_occupation(self):
        data = {
            'tracking_id': self.application_obj.tracking_id,
            'occupation': 'invalid',
            'organization': self.fake_data.company(),
            'from_date': self.fake_data.date(),
            'to_date': self.fake_data.date(),
            'description': self.fake_data.text(),
        }
        response = self.client.post(
            self.create_latest_occupation_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                'occupation': ['"invalid" is not a valid choice.'],
            }
        )

    def create_latest_occupation(self):
        data = {
            'tracking_id': self.application_obj.tracking_id,
            'occupation': self.fake_data.random_choices(self.occupation, 1)[0],
            'organization': self.fake_data.company(),
            'from_date': self.fake_data.date(),
            'to_date': self.fake_data.date(),
            'description': self.fake_data.text(),
        }
        response = self.client.post(
            self.create_latest_occupation_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LatestOccupationModel.objects.count(), 1)
        try:
            latest_occupation = LatestOccupationModel.objects.get(application=self.application_obj)
            self.assertIsNotNone(latest_occupation)
            response_json = response.json()
            data['from_date'] = datetime.strptime(data['from_date'], '%Y-%m-%d').date()
            data['to_date'] = datetime.strptime(data['to_date'], '%Y-%m-%d').date()
            data.pop('tracking_id')
            self.assertEqual(response_json, LatestOccupationSerializer(latest_occupation, many=False).data)
            for key, value in data.items():
                self.assertEqual(getattr(latest_occupation, key), value)
        except LatestOccupationModel.DoesNotExist:
            self.assertTrue(False)

    def retrieve_latest_occupation(self):
        response = self.client.get(
            self._detail_update_latest_occupation_api(self.application_obj.tracking_id),
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        latest_occupation = LatestOccupationModel.objects.get(application=self.application_obj)
        self.assertIsNotNone(latest_occupation)
        self.assertEqual(response_json, LatestOccupationSerializer(latest_occupation, many=False).data)

    def update_latest_occupation(self):
        data = {
            'occupation': self.fake_data.random_choices(self.occupation, 1)[0],
            'organization': self.fake_data.company(),
        }
        response = self.client.put(
            self._detail_update_latest_occupation_api(self.application_obj.tracking_id),
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        try:
            latest_occupation = LatestOccupationModel.objects.get(application=self.application_obj)
            self.assertIsNotNone(latest_occupation)
            response_json = response.json()
            self.assertEqual(response_json, LatestOccupationSerializer(latest_occupation, many=False).data)
            for key, value in data.items():
                self.assertEqual(getattr(latest_occupation, key), value)
        except LatestOccupationModel.DoesNotExist:
            self.assertTrue(False)
