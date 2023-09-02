from django.test import Client
from django.urls import reverse

from rest_framework.test import APITestCase

from faker import Faker


class TestOccupationSetUp(APITestCase):
    def setUp(self):
        self.client = Client()
        self.fake_data = Faker()

        self.create_latest_occupation_api = reverse('app_occupation:occupation_create', kwargs={"version": "v1"})

        super(TestOccupationSetUp, self).setUp()

    def _detail_update_latest_occupation_api(self, tracking_id):
        return reverse('app_occupation:occupation_detail_update', kwargs={"version": "v1", "tracking_id": tracking_id})

    def tearDown(self):
        super(TestOccupationSetUp, self).tearDown()
