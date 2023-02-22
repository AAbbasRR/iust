from django.test import Client
from django.urls import reverse

from rest_framework.test import APITestCase


class TestApplicationSetUp(APITestCase):
    def setUp(self):
        self.client = Client()

        super(TestApplicationSetUp, self).setUp()

    def tearDown(self):
        super(TestApplicationSetUp, self).tearDown()
