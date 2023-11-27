from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.authtoken.models import Token

from app_application.tests import TestApplicationSetUp

from app_application.models import ApplicationModel, DocumentModel

from utils import BaseErrors
import json

UserModel = get_user_model()


class UserDocumentsApiTestCase(TestApplicationSetUp):
    def setUp(self):
        super(UserDocumentsApiTestCase, self).setUp()

        self.success_profile = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }
        self.user_obj = UserModel.objects.register_user(
            email=self.success_profile["email"],
            password=self.success_profile["password"],
        )
        self.user_obj.activate()
        self.user_token = Token.objects.get(user=self.user_obj)

        self.application_obj = ApplicationModel.objects.create(user=self.user_obj)

    def test_methods(self):
        self.create_invalid_tracking_id()
        self.create_document()
        self.retrieve_document()

    def create_invalid_tracking_id(self):
        data = {
            "tracking_id": "invalid_id",
            "curriculum_vitae": self._create_image(),
            "personal_photo": self._create_image(),
            "valid_passport": self._create_image(),
            "high_school_certificate": self._create_image(),
        }
        response = self.client.post(
            self.create_document_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
            format="multipart",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_json = response.json()
        self.assertEqual(response_json, {"detail": BaseErrors.tracking_id_not_found})

    def create_document(self):
        data = {
            "tracking_id": self.application_obj.tracking_id,
            "curriculum_vitae": self._create_image(),
            "personal_photo": self._create_image(),
            "valid_passport": self._create_image(),
            "high_school_certificate": self._create_image(),
        }
        response = self.client.post(
            self.create_document_api,
            data,
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
            format="multipart/form-data",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DocumentModel.objects.count(), 1)
        try:
            document = DocumentModel.objects.get(application=self.application_obj)
            self.assertIsNotNone(document)
            self.create_response_json = response.json()
        except DocumentModel.DoesNotExist:
            self.assertTrue(False)

    def retrieve_document(self):
        response = self.client.get(
            self._detail_update_document_api(self.application_obj.tracking_id),
            HTTP_AUTHORIZATION=f"Token {self.user_token.key}",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.json()
        self.assertEqual(response_json, self.create_response_json)
