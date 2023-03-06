from django.contrib.auth import get_user_model

from app_education.models import ProgramRequestedModel
from app_education.tests import TestEducationSetUp
from app_application.models import ApplicationModel

from utils.data_list import degree_options, faculty_options, field_of_study_options

UserModel = get_user_model()


class ProgramRequestedTestCase(TestEducationSetUp):
    def setUp(self):
        super(ProgramRequestedTestCase, self).setUp()

        self.success_user = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }
        self.user_obj = UserModel.objects.register_user(
            email=self.success_user['email'],
            password=self.success_user['password']
        )
        self.user_obj.activate()

        self.application_obj = ApplicationModel.objects.create(
            user=self.user_obj,
        )

        self.degree = [value[0] for value in degree_options]
        self.faculty = [value[0] for value in faculty_options]
        self.field_of_study = [value[0] for value in field_of_study_options]

    def test_methods(self):
        self.create_test()
        self.delete_user_test()

    def create_test(self):
        program_requested_count = ProgramRequestedModel.objects.all().count()
        self.assertEqual(program_requested_count, 0)
        data = {
            "degree": self.fake_data.random_choices(self.degree, 1)[0],
            "faculty": self.fake_data.random_choices(self.faculty, 1)[0],
            "field_of_study": self.fake_data.random_choices(self.field_of_study, 1)[0],
        }
        self.success_program_requested_obj = ProgramRequestedModel.objects.create(
            application=self.application_obj,
            **data
        )
        self.assertIsNotNone(self.success_program_requested_obj)
        self.assertEqual(self.success_program_requested_obj.application.user.email, self.user_obj.email)
        self.assertEqual(self.success_program_requested_obj.degree, data['degree'])
        self.assertEqual(self.success_program_requested_obj.faculty, data['faculty'])
        self.assertEqual(self.success_program_requested_obj.field_of_study, data['field_of_study'])
        program_requested_count = ProgramRequestedModel.objects.all().count()
        self.assertEqual(program_requested_count, 1)

    def delete_user_test(self):
        self.success_program_requested_obj.delete()
        program_requested_count = ProgramRequestedModel.objects.all().count()
        self.assertEqual(program_requested_count, 0)
