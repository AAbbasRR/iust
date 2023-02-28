from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.authtoken.models import Token

from app_education.tests import TestEducationSetUp

from app_education.models import HighSchoolModel
from app_education.api.serializers.high_school import HighSchoolSerializer

from datetime import datetime

UserModel = get_user_model()


class UserHighSchoolApiTestCase(TestEducationSetUp):

    def setUp(self):
        super(UserHighSchoolApiTestCase, self).setUp()

        self.success_profile = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }
        self.user_obj = UserModel.objects.register_user(email=self.success_profile['email'], password=self.success_profile['password'])
        self.user_obj.activate()
        self.user_token = Token.objects.get(user=self.user_obj)

    def test_methods(self):
        self.create_high_school_missing_fields()
        self.create_high_school()
        self.retrieve_high_school()
        self.update_high_school()

    def create_high_school_missing_fields(self):
        response = self.client.post(
            self.create_high_school_api,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                'date_of_graduation': ['This field is required.'],
                'gpa': ['This field is required.'],
                'field_of_study': ['This field is required.'],
            }
        )

    def create_high_school(self):
        data = {
            'date_of_graduation': self.fake_data.date(),
            'gpa': self.fake_data.pyfloat(left_digits=2, right_digits=2, positive=True, min_value=1, max_value=100),
            'field_of_study': self.fake_data.job(),
        }
        response = self.client.post(
            self.create_high_school_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HighSchoolModel.objects.count(), 1)
        try:
            high_school = HighSchoolModel.objects.get(user=self.user_obj)
            self.assertIsNotNone(high_school)
            response_json = response.json()
            data['date_of_graduation'] = datetime.strptime(data['date_of_graduation'], '%Y-%m-%d').date()
            self.assertEqual(response_json, HighSchoolSerializer(high_school, many=False).data)
            for key, value in data.items():
                self.assertEqual(getattr(high_school, key), value)
        except HighSchoolModel.DoesNotExist:
            self.assertTrue(False)

    def retrieve_high_school(self):
        response = self.client.get(
            self.detail_update_high_school_api,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        high_school = HighSchoolModel.objects.get(user=self.user_obj)
        self.assertIsNotNone(high_school)
        self.assertEqual(response_json, HighSchoolSerializer(high_school, many=False).data)

    def update_high_school(self):
        data = {
            'gpa': self.fake_data.pyfloat(left_digits=2, right_digits=2, positive=True, min_value=1, max_value=100),
            'field_of_study': self.fake_data.job(),
        }
        response = self.client.put(
            self.detail_update_high_school_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        try:
            high_school = HighSchoolModel.objects.get(user=self.user_obj)
            self.assertIsNotNone(high_school)
            response_json = response.json()
            self.assertEqual(response_json, HighSchoolSerializer(high_school, many=False).data)
            for key, value in data.items():
                self.assertEqual(getattr(high_school, key), value)
        except HighSchoolModel.DoesNotExist:
            self.assertTrue(False)
