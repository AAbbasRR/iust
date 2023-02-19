from django.test import Client
from django.urls import reverse

from rest_framework.test import APITestCase


class TestEducationSetUp(APITestCase):
    def setUp(self):
        self.client = Client()

        super(TestEducationSetUp, self).setUp()

    def tearDown(self):
        super(TestEducationSetUp, self).tearDown()
