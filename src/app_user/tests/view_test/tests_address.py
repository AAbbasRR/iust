from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.authtoken.models import Token

from app_user.tests import TestUserSetUp

from app_user.models import AddressModel
from app_user.api.serializers.address import AddressSerializer

from utils.data_list import country

from faker import Faker

UserModel = get_user_model()


class UserAddressApiTestCase(TestUserSetUp):

    def setUp(self):
        super(UserAddressApiTestCase, self).setUp()

        self.fake_data = Faker()

        self.success_profile = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }
        self.user_obj = UserModel.objects.register_user(email=self.success_profile['email'], password=self.success_profile['password'])
        self.user_obj.activate()
        self.user_token = Token.objects.get(user=self.user_obj)

        countries = [value[0] for value in country]

        self.address_data = {
            'country': self.fake_data.random_choices(countries, 1)[0],
            'city': self.fake_data.city(),
            'country_code': self.fake_data.country_code(),
            'postal_code': self.fake_data.postcode(),
            'city_code': self.fake_data.country_code(),
            'phone_number': self.fake_data.phone_number(),
            'address': self.fake_data.address(),
        }
        self.updated_address_data = {
            'country': self.fake_data.random_choices(countries, 1)[0],
            'postal_code': self.fake_data.postcode(),
            'city_code': self.fake_data.country_code(),
            'address': self.fake_data.address(),
        }

    def test_methods(self):
        self.create_address_missing_fields()
        self.create_address_invalid_country()
        self.create_address()
        self.retrieve_address()
        self.update_address()

    def create_address_missing_fields(self):
        response = self.client.post(
            self.create_address_api,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                'country': ['This field is required.'],
                'city': ['This field is required.'],
                'postal_code': ['This field is required.'],
                'address': ['This field is required.'],
            }
        )

    def create_address_invalid_country(self):
        data = {**self.address_data, 'country': 'invalid'}
        response = self.client.post(
            self.create_address_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                'country': ['"invalid" is not a valid choice.'],
            }
        )

    def create_address(self):
        response = self.client.post(
            self.create_address_api,
            self.address_data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AddressModel.objects.count(), 1)
        try:
            address = AddressModel.objects.get(user=self.user_obj)
            self.assertIsNotNone(address)
            response_json = response.json()
            self.assertEqual(response_json, AddressSerializer(address, many=False).data)
            for key, value in self.address_data.items():
                self.assertEqual(getattr(address, key), value)
        except AddressModel.DoesNotExist:
            self.assertTrue(False)

    def retrieve_address(self):
        response = self.client.get(
            self.detail_update_address_api,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        address = AddressModel.objects.get(user=self.user_obj)
        self.assertIsNotNone(address)
        self.assertEqual(response_json, AddressSerializer(address, many=False).data)

    def update_address(self):
        response = self.client.put(
            self.detail_update_address_api,
            self.updated_address_data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        try:
            address = AddressModel.objects.get(user=self.user_obj)
            self.assertIsNotNone(address)
            response_json = response.json()
            self.assertEqual(response_json, AddressSerializer(address, many=False).data)
            for key, value in self.updated_address_data.items():
                self.assertEqual(getattr(address, key), value)
        except AddressModel.DoesNotExist:
            self.assertTrue(False)
