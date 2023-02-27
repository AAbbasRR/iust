from django.test import Client
from django.urls import reverse

from rest_framework.test import APITestCase


class TestApplicationSetUp(APITestCase):
    def setUp(self):
        self.client = Client()
        self.list_all_user_application_api = reverse('app_application:application_all_list', kwargs={"version": "v1"})
        self.create_application_api = reverse('app_application:application_create', kwargs={"version": "v1"})

        super(TestApplicationSetUp, self).setUp()

    def detail_update_application_api(self, tracking_id):
        return reverse('app_application:application_detail_update', kwargs={"version": "v1", "tracking_id": tracking_id})

    def tearDown(self):
        super(TestApplicationSetUp, self).tearDown()
