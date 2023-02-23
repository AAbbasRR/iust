from django.test import Client
from django.urls import reverse

from rest_framework.test import APITestCase


class TestOccupationSetUp(APITestCase):
    def setUp(self):
        self.client = Client()

        super(TestOccupationSetUp, self).setUp()

    def tearDown(self):
        super(TestOccupationSetUp, self).tearDown()
