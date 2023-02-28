from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.authtoken.models import Token

from app_application.tests import TestApplicationSetUp

from app_application.models import ApplicationModel
from app_application.api.serializers.application import ApplicationSerializer

UserModel = get_user_model()


class UserApplicationApiTestCase(TestApplicationSetUp):

    def setUp(self):
        super(UserApplicationApiTestCase, self).setUp()

        self.success_profile = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }
        self.user_obj = UserModel.objects.register_user(email=self.success_profile['email'], password=self.success_profile['password'])
        self.user_obj.activate()
        self.user_token = Token.objects.get(user=self.user_obj)

        self.application_data = {
            'full_name': f'{self.fake_data.first_name()} {self.fake_data.last_name()}',
            'comments': self.fake_data.text(),
            'applied_program': self.fake_data.random_choices([True, False], 1)[0],
            'financial_self_support': self.fake_data.random_choices([True, False], 1)[0],
        }
        self.updated_application_data = {
            'full_name': f'{self.fake_data.first_name()} {self.fake_data.last_name()}',
            'comments': self.fake_data.text(),
            'applied_program': self.fake_data.random_choices([True, False], 1)[0],
            'financial_self_support': self.fake_data.random_choices([True, False], 1)[0],
        }

    def test_methods(self):
        self.create_application()
        self.list_all_applications()
        self.retrieve_application()
        self.update_application()

    def create_application(self):
        response = self.client.post(
            self.create_application_api,
            self.application_data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ApplicationModel.objects.count(), 1)
        try:
            application = ApplicationModel.objects.get(user=self.user_obj)
            self.assertIsNotNone(application)
            response_json = response.json()
            self.assertEqual(response_json, ApplicationSerializer(application, many=False).data)
            for key, value in self.application_data.items():
                self.assertEqual(getattr(application, key), value)
        except ApplicationModel.DoesNotExist:
            self.assertTrue(False)

    def list_all_applications(self):
        response = self.client.get(
            self.list_all_user_application_api,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        try:
            application = ApplicationModel.objects.get(user=self.user_obj)
            self.assertIsNotNone(application)
            response_json = response.json()
            self.assertEqual(response_json, [ApplicationSerializer(application, many=False).data])
            for key, value in self.application_data.items():
                self.assertEqual(getattr(application, key), value)

            self.tracking_id = application.tracking_id
        except ApplicationModel.DoesNotExist:
            self.assertTrue(False)

    def retrieve_application(self):
        response = self.client.get(
            self._detail_update_application_api(self.tracking_id),
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        application = ApplicationModel.objects.get(user=self.user_obj)
        self.assertIsNotNone(application)
        self.assertEqual(response_json, ApplicationSerializer(application, many=False).data)

    def update_application(self):
        response = self.client.put(
            self._detail_update_application_api(self.tracking_id),
            self.updated_application_data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        try:
            application = ApplicationModel.objects.get(user=self.user_obj)
            self.assertIsNotNone(application)
            response_json = response.json()
            self.assertEqual(response_json, ApplicationSerializer(application, many=False).data)
            for key, value in self.updated_application_data.items():
                self.assertEqual(getattr(application, key), value)
        except ApplicationModel.DoesNotExist:
            self.assertTrue(False)
