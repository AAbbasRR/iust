from django.contrib.auth import get_user_model

from app_education.models import HighSchoolModel
from app_education.tests import TestEducationSetUp

from faker import Faker
from datetime import datetime

UserModel = get_user_model()


class HighSchoolTestCase(TestEducationSetUp):
    def setUp(self):
        super(HighSchoolTestCase, self).setUp()

        self.fake_data = Faker()

        self.success_user = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }

        self.user_obj = UserModel.objects.register_user(
            email=self.success_user["email"], password=self.success_user["password"]
        )
        self.user_obj.activate()

    def test_methods(self):
        self.create_test()
        self.delete_user_test()

    def create_test(self):
        high_school_count = HighSchoolModel.objects.all().count()
        self.assertEqual(high_school_count, 0)
        data = {
            "date_of_graduation": datetime.now().date(),
            "gpa": self.fake_data.random_number(2),
            "field_of_study": "computer engineer",
        }
        self.success_high_school_obj = HighSchoolModel.objects.create(
            user=self.user_obj, **data
        )
        self.assertIsNotNone(self.success_high_school_obj)
        self.assertEqual(self.success_high_school_obj.user.email, self.user_obj.email)
        self.assertEqual(
            self.success_high_school_obj.date_of_graduation, data["date_of_graduation"]
        )
        self.assertEqual(self.success_high_school_obj.gpa, data["gpa"])
        self.assertEqual(
            self.success_high_school_obj.field_of_study, data["field_of_study"]
        )

        high_school_count = HighSchoolModel.objects.all().count()
        self.assertEqual(high_school_count, 1)

    def delete_user_test(self):
        self.user_obj.delete()
        high_school_count = HighSchoolModel.objects.all().count()
        self.assertEqual(high_school_count, 0)
