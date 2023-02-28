from django.test import Client
from django.urls import reverse

from rest_framework.test import APITestCase

from faker import Faker


class TestEducationSetUp(APITestCase):
    def setUp(self):
        self.client = Client()
        self.fake_data = Faker()

        self.create_high_school_api = reverse('app_education:education_high_school_create', kwargs={"version": "v1"})
        self.detail_update_high_school_api = reverse('app_education:education_high_school_detail_update', kwargs={"version": "v1"})

        super(TestEducationSetUp, self).setUp()

    def tearDown(self):
        super(TestEducationSetUp, self).tearDown()
