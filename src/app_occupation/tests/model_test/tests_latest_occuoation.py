from django.contrib.auth import get_user_model

from app_application.models import ApplicationModel
from app_occupation.models import LatestOccupationModel
from app_occupation.tests import TestOccupationSetUp

from faker import Faker
from datetime import datetime

User = get_user_model()


class LatestOccupationTestCase(TestOccupationSetUp):
    def setUp(self):
        super(LatestOccupationTestCase, self).setUp()

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

        self.success_application = {
            "full_name": f'{self.fake_data.first_name()} {self.fake_data.last_name()}',
            "comments": self.fake_data.random_choices(['', self.fake_data.text()], 1)[0],
            "applied_program": self.fake_data.random_choices([True, False], 1)[0],
            "financial_self_support": self.fake_data.random_choices([True, False], 1)[0],
            "status": self.fake_data.random_choices(['CRNT', 'ACPT', 'RJCT', 'NTET'], 1)[0],
        }
        self.success_application_obj = ApplicationModel.objects.create(
            user=self.user_obj,
            **self.success_application
        )

    def test_methods(self):
        self.create_test()
        self.delete_user_test()

    def create_test(self):
        sql_count = LatestOccupationModel.objects.all().count()
        self.assertEqual(sql_count, 0)
        data = {
            "occupation": self.fake_data.random_choices(['ACD', 'GVE', 'INE', 'STU', 'OTR'], 1)[0],
            "organization": 'microsoft',
            "from_date": datetime.strptime('2018-03-14', '%Y-%m-%d'),
            "to_date": datetime.strptime('2021-07-21', '%Y-%m-%d'),
            "description": self.fake_data.text(),
        }
        self.success_occupation_obj = LatestOccupationModel.objects.create(
            application=self.success_application_obj,
            **data
        )
        self.assertIsNotNone(self.success_occupation_obj)
        self.assertEqual(self.success_occupation_obj.application.user.email, self.user_obj.email)
        self.assertEqual(self.success_occupation_obj.occupation, data['occupation'])
        self.assertEqual(self.success_occupation_obj.organization, data['organization'])
        self.assertEqual(self.success_occupation_obj.from_date, data['from_date'])
        self.assertEqual(self.success_occupation_obj.to_date, data['to_date'])
        self.assertEqual(self.success_occupation_obj.description, data['description'])

        sql_count = LatestOccupationModel.objects.all().count()
        self.assertEqual(sql_count, 1)

    def delete_user_test(self):
        self.user_obj.delete()
        sql_count = LatestOccupationModel.objects.all().count()
        self.assertEqual(sql_count, 0)
