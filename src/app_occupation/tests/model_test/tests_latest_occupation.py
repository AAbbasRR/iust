from django.contrib.auth import get_user_model

from app_occupation.models import LatestOccupationModel
from app_occupation.tests import TestOccupationSetUp

from datetime import datetime

UserModel = get_user_model()


class LatestOccupationTestCase(TestOccupationSetUp):
    def setUp(self):
        super(LatestOccupationTestCase, self).setUp()

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
        sql_count = LatestOccupationModel.objects.all().count()
        self.assertEqual(sql_count, 0)
        data = {
            "occupation": self.fake_data.random_choices(
                ["ACD", "GVE", "INE", "STU", "OTR"], 1
            )[0],
            "organization": "microsoft",
            "from_date": datetime.strptime("2018-03-14", "%Y-%m-%d"),
            "to_date": datetime.strptime("2021-07-21", "%Y-%m-%d"),
            "description": self.fake_data.text(),
        }
        self.success_occupation_obj = LatestOccupationModel.objects.create(
            user=self.user_obj, **data
        )
        self.assertIsNotNone(self.success_occupation_obj)
        self.assertEqual(self.success_occupation_obj.user.email, self.user_obj.email)
        self.assertEqual(self.success_occupation_obj.occupation, data["occupation"])
        self.assertEqual(self.success_occupation_obj.organization, data["organization"])
        self.assertEqual(self.success_occupation_obj.from_date, data["from_date"])
        self.assertEqual(self.success_occupation_obj.to_date, data["to_date"])
        self.assertEqual(self.success_occupation_obj.description, data["description"])

        sql_count = LatestOccupationModel.objects.all().count()
        self.assertEqual(sql_count, 1)

    def delete_user_test(self):
        self.user_obj.delete()
        sql_count = LatestOccupationModel.objects.all().count()
        self.assertEqual(sql_count, 0)
