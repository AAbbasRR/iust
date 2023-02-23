from django.contrib.auth import get_user_model

from app_application.models import ApplicationModel
from app_application.tests import TestApplicationSetUp

from faker import Faker

User = get_user_model()


class ApplicationTestCase(TestApplicationSetUp):
    def setUp(self):
        super(ApplicationTestCase, self).setUp()

        self.fake_data = Faker()

        self.success_user = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }

        self.user_obj = User.objects.register_user(
            email=self.success_user['email'],
            password=self.success_user['password']
        )
        self.user_obj.activate()

    def test_methods(self):
        self.create_test()
        self.delete_user_test()

    def create_test(self):
        sql_count = ApplicationModel.objects.all().count()
        self.assertEqual(sql_count, 0)
        data = {
            "full_name": f'{self.fake_data.first_name()} {self.fake_data.last_name()}',
            "comments": self.fake_data.random_choices(['', self.fake_data.text()], 1)[0],
            "applied_program": self.fake_data.random_choices([True, False], 1)[0],
            "financial_self_support": self.fake_data.random_choices([True, False], 1)[0],
            "status": self.fake_data.random_choices(['CRNT', 'ACPT', 'RJCT', 'NTET'], 1)[0],
        }
        self.success_application_obj = ApplicationModel.objects.create(
            user=self.user_obj,
            **data
        )
        self.assertIsNotNone(self.success_application_obj)
        self.assertEqual(self.success_application_obj.user.email, self.user_obj.email)
        self.assertEqual(self.success_application_obj.full_name, data['full_name'])
        self.assertEqual(self.success_application_obj.comments, data['comments'])
        self.assertEqual(self.success_application_obj.applied_program, data['applied_program'])
        self.assertEqual(self.success_application_obj.financial_self_support, data['financial_self_support'])
        self.assertEqual(self.success_application_obj.status, data['status'])

        sql_count = ApplicationModel.objects.all().count()
        self.assertEqual(sql_count, 1)

    def delete_user_test(self):
        self.user_obj.delete()
        sql_count = ApplicationModel.objects.all().count()
        self.assertEqual(sql_count, 0)
