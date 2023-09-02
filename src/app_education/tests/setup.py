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

        self.create_bachelor_degree_api = reverse('app_education:education_bachelor_degree_create', kwargs={"version": "v1"})
        self.detail_update_bachelor_degree_api = reverse('app_education:education_bachelor_degree_detail_update', kwargs={"version": "v1"})

        self.create_master_degree_api = reverse('app_education:education_master_degree_create', kwargs={"version": "v1"})
        self.detail_update_master_degree_api = reverse('app_education:education_master_degree_detail_update', kwargs={"version": "v1"})

        self.create_program_requested_api = reverse('app_education:education_program_requested_create', kwargs={"version": "v1"})

        super(TestEducationSetUp, self).setUp()

    def _detail_update_program_requested_api(self, tracking_id):
        return reverse('app_education:education_program_requested_detail_update', kwargs={"version": "v1", "tracking_id": tracking_id})

    def tearDown(self):
        super(TestEducationSetUp, self).tearDown()
