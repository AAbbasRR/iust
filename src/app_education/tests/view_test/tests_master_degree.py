from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.authtoken.models import Token

from app_education.tests import TestEducationSetUp

from app_education.models import MasterDegreeModel
from app_education.api.serializers.master_degree import MasterDegreeSerializer

from utils.data_list import country
from datetime import datetime

UserModel = get_user_model()


class UserMasterDegreeApiTestCase(TestEducationSetUp):
    def setUp(self):
        super(UserMasterDegreeApiTestCase, self).setUp()

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

        self.countries = [value[0] for value in country]

    def test_methods(self):
        self.create_master_degree_missing_fields()
        self.create_master_degree_invalid_country()
        self.create_master_degree()
        self.retrieve_master_degree()
        self.update_master_degree()

    def create_master_degree_missing_fields(self):
        response = self.client.post(
            self.create_master_degree_api,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                "country": ["This field is required."],
                "city": ["This field is required."],
                "date_of_graduation": ["This field is required."],
                "gpa": ["This field is required."],
                "field_of_study": ["This field is required."],
                "university": ["This field is required."],
            },
        )

    def create_master_degree_invalid_country(self):
        data = {
            "country": "invalid",
            "city": self.fake_data.city(),
            "date_of_graduation": self.fake_data.date(),
            "gpa": self.fake_data.pyfloat(
                left_digits=2, right_digits=2, positive=True, min_value=1, max_value=100
            ),
            "field_of_study": self.fake_data.job(),
            "university": self.fake_data.text(max_nb_chars=50),
        }
        response = self.client.post(
            self.create_master_degree_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                "country": ['"invalid" is not a valid choice.'],
            },
        )

    def create_master_degree(self):
        data = {
            "country": self.fake_data.random_choices(self.countries, 1)[0],
            "city": self.fake_data.city(),
            "date_of_graduation": self.fake_data.date(),
            "gpa": self.fake_data.pyfloat(
                left_digits=2, right_digits=2, positive=True, min_value=1, max_value=100
            ),
            "field_of_study": self.fake_data.job(),
            "university": self.fake_data.text(max_nb_chars=50),
        }
        response = self.client.post(
            self.create_master_degree_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MasterDegreeModel.objects.count(), 1)
        try:
            master_degree = MasterDegreeModel.objects.get(user=self.user_obj)
            self.assertIsNotNone(master_degree)
            response_json = response.json()
            data["date_of_graduation"] = datetime.strptime(
                data["date_of_graduation"], "%Y-%m-%d"
            ).date()
            self.assertEqual(
                response_json, MasterDegreeSerializer(master_degree, many=False).data
            )
            for key, value in data.items():
                self.assertEqual(getattr(master_degree, key), value)
        except MasterDegreeModel.DoesNotExist:
            self.assertTrue(False)

    def retrieve_master_degree(self):
        response = self.client.get(
            self.detail_update_master_degree_api,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        master_degree = MasterDegreeModel.objects.get(user=self.user_obj)
        self.assertIsNotNone(master_degree)
        self.assertEqual(
            response_json, MasterDegreeSerializer(master_degree, many=False).data
        )

    def update_master_degree(self):
        data = {
            "gpa": self.fake_data.pyfloat(
                left_digits=2, right_digits=2, positive=True, min_value=1, max_value=100
            ),
            "field_of_study": self.fake_data.job(),
        }
        response = self.client.put(
            self.detail_update_master_degree_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        try:
            master_degree = MasterDegreeModel.objects.get(user=self.user_obj)
            self.assertIsNotNone(master_degree)
            response_json = response.json()
            self.assertEqual(
                response_json, MasterDegreeSerializer(master_degree, many=False).data
            )
            for key, value in data.items():
                self.assertEqual(getattr(master_degree, key), value)
        except MasterDegreeModel.DoesNotExist:
            self.assertTrue(False)
