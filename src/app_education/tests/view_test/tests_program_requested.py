from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.authtoken.models import Token

from app_education.tests import TestEducationSetUp

from app_education.models import ProgramRequestedModel
from app_education.api.serializers.program_requested import ProgramRequestedSerializer
from app_application.models import ApplicationModel

from utils import BaseErrors
from utils.data_list import degree_options, faculty_options, field_of_study_options, program_requested_data

UserModel = get_user_model()


class ProgramRequestedApiTestCase(TestEducationSetUp):

    def setUp(self):
        super(ProgramRequestedApiTestCase, self).setUp()

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

        self.degree = [value[0] for value in degree_options]
        self.faculty = [value[0] for value in faculty_options]
        self.field_of_study = [value[0] for value in field_of_study_options]

    def test_methods(self):
        self.create_program_requested_missing_fields()
        self.create_invalid_tracking_id()
        self.create_program_requested_invalid_degree()
        self.create_program_requested_invalid_faculty()
        self.create_program_requested_invalid_field_of_study()
        self.create_program_request()
        self.retrieve_program_request()
        self.update_program_request()

    def create_program_requested_missing_fields(self):
        response = self.client.post(
            self.create_program_requested_api,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                'tracking_id': ['This field is required.'],
                'degree': ['This field is required.'],
                'faculty': ['This field is required.'],
                'field_of_study': ['This field is required.'],
            }
        )

    def create_invalid_tracking_id(self):
        data = {
            'tracking_id': "invalid_id",
            'degree': self.fake_data.random_choices(self.degree, 1)[0],
            'faculty': self.fake_data.random_choices(self.faculty, 1)[0],
            'field_of_study': self.fake_data.random_choices(self.field_of_study, 1)[0],
        }
        response = self.client.post(
            self.create_program_requested_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_json = response.json()
        self.assertEqual(response_json, {
            'detail': BaseErrors.tracking_id_not_found
        })

    def create_program_requested_invalid_degree(self):
        data = {
            'tracking_id': self.application_obj.tracking_id,
            'degree': 'invalid',
            'faculty': self.fake_data.random_choices(self.faculty, 1)[0],
            'field_of_study': self.fake_data.random_choices(self.field_of_study, 1)[0],
        }
        response = self.client.post(
            self.create_program_requested_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                'degree': ['"invalid" is not a valid choice.'],
            }
        )

    def create_program_requested_invalid_faculty(self):
        data = {
            'tracking_id': self.application_obj.tracking_id,
            'degree': self.fake_data.random_choices(self.degree, 1)[0],
            'faculty': 'invalid',
            'field_of_study': self.fake_data.random_choices(self.field_of_study, 1)[0],
        }
        response = self.client.post(
            self.create_program_requested_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                'faculty': ['"invalid" is not a valid choice.'],
            }
        )

        while True:
            try:
                degree_faculties = [value[0] for value in program_requested_data[data['degree']]['items']]
                faculty_items = list(filter(lambda value: value not in degree_faculties, self.faculty))
                data = {**data, 'faculty': self.fake_data.random_choices(faculty_items, 1)[0]}
                break
            except IndexError:
                data = {**data, 'degree': self.fake_data.random_choices(self.degree, 1)[0]}
        response = self.client.post(
            self.create_program_requested_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                'faculty': [BaseErrors._change_error_variable('invalid_choice_value', input=data['faculty'])],
            }
        )

    def create_program_requested_invalid_field_of_study(self):
        data = {
            'tracking_id': self.application_obj.tracking_id,
            'degree': self.fake_data.random_choices(self.degree, 1)[0],
            'faculty': self.fake_data.random_choices(self.faculty, 1)[0],
            'field_of_study': 'invalid',
        }
        response = self.client.post(
            self.create_program_requested_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                'field_of_study': ['"invalid" is not a valid choice.'],
            }
        )

        faculty = self.fake_data.random_choices(program_requested_data[data['degree']]['items'], 1)[0][0]
        faculty_fields = [value[0] for value in program_requested_data[data['degree']]['data'][faculty]]
        field_of_study_items = list(filter(lambda value: value not in faculty_fields, self.field_of_study))
        data = {
            **data,
            'faculty': faculty,
            'field_of_study': self.fake_data.random_choices(field_of_study_items, 1)[0]
        }
        response = self.client.post(
            self.create_program_requested_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_json = response.json()
        self.assertEqual(
            response_json,
            {
                'field_of_study': [BaseErrors._change_error_variable('invalid_choice_value', input=data['field_of_study'])],
            }
        )

    def create_program_request(self):
        degree = self.fake_data.random_choices(self.degree, 1)[0]
        faculty = self.fake_data.random_choices(program_requested_data[degree]['items'], 1)[0][0]
        field_of_study = self.fake_data.random_choices(program_requested_data[degree]['data'][faculty], 1)[0][0]
        data = {
            'tracking_id': self.application_obj.tracking_id,
            'degree': degree,
            'faculty': faculty,
            'field_of_study': field_of_study,
        }
        response = self.client.post(
            self.create_program_requested_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProgramRequestedModel.objects.count(), 1)
        try:
            program_request = ProgramRequestedModel.objects.get(application=self.application_obj)
            self.assertIsNotNone(program_request)
            response_json = response.json()
            data.pop('tracking_id')
            self.assertEqual(response_json, ProgramRequestedSerializer(program_request, many=False).data)
            for key, value in data.items():
                self.assertEqual(getattr(program_request, key), value)
        except ProgramRequestedModel.DoesNotExist:
            self.assertTrue(False)

    def retrieve_program_request(self):
        response = self.client.get(
            self._detail_update_program_requested_api(self.application_obj.tracking_id),
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        program_request = ProgramRequestedModel.objects.get(application=self.application_obj)
        self.assertIsNotNone(program_request)
        self.assertEqual(response_json, ProgramRequestedSerializer(program_request, many=False).data)

    def update_program_request(self):
        degree = self.fake_data.random_choices(self.degree, 1)[0]
        faculty = self.fake_data.random_choices(program_requested_data[degree]['items'], 1)[0][0]
        field_of_study = self.fake_data.random_choices(program_requested_data[degree]['data'][faculty], 1)[0][0]
        data = {
            'degree': degree,
            'faculty': faculty,
            'field_of_study': field_of_study,
        }
        response = self.client.put(
            self._detail_update_program_requested_api(self.application_obj.tracking_id),
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        try:
            program_request = ProgramRequestedModel.objects.get(application=self.application_obj)
            self.assertIsNotNone(program_request)
            response_json = response.json()
            self.assertEqual(response_json, ProgramRequestedSerializer(program_request, many=False).data)
            for key, value in data.items():
                self.assertEqual(getattr(program_request, key), value)
        except ProgramRequestedModel.DoesNotExist:
            self.assertTrue(False)
