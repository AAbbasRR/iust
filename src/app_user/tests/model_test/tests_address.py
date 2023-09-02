from django.contrib.auth import get_user_model

from app_user.models import AddressModel
from app_user.tests import TestUserSetUp

UserModel = get_user_model()


class AddressTestCase(TestUserSetUp):
    def setUp(self):
        super(AddressTestCase, self).setUp()

        self.success_user = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }

        self.user_obj = UserModel.objects.register_user(
            email=self.success_user['email'],
            password=self.success_user['password']
        )
        self.user_obj.activate()

    def test_methods(self):
        self.create_test()
        self.delete_user_test()

    def create_test(self):
        address_count = AddressModel.objects.all().count()
        self.assertEqual(address_count, 0)
        data = {
            "country_code": self.fake_data.country_code(),
            "postal_code": self.fake_data.postcode(),
            "city_code": self.fake_data.country_code(),
            "address": self.fake_data.address(),
            "country": self.fake_data.country(),
            "city": self.fake_data.city(),
        }
        self.success_address_obj = AddressModel.objects.create(
            user=self.user_obj,
            **data
        )
        self.assertIsNotNone(self.success_address_obj)
        self.assertEqual(self.success_address_obj.user.email, self.user_obj.email)
        self.assertEqual(self.success_address_obj.address, data['address'])
        self.assertEqual(self.success_address_obj.country, data['country'])
        self.assertEqual(self.success_address_obj.postal_code, data['postal_code'])
        self.assertEqual(self.success_address_obj.city, data['city'])
        address_count = AddressModel.objects.all().count()
        self.assertEqual(address_count, 1)

    def delete_user_test(self):
        self.user_obj.delete()
        address_count = AddressModel.objects.all().count()
        self.assertEqual(address_count, 0)
