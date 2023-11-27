from django.contrib.auth import get_user_model

from app_application.models import ApplicationModel, DocumentModel
from app_application.tests import TestApplicationSetUp

from Abrat.settings import BASE_DIR

import os

UserModel = get_user_model()


class DocumentTestCase(TestApplicationSetUp):
    def setUp(self):
        super(DocumentTestCase, self).setUp()

        self.success_user = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }
        self.user_obj = UserModel.objects.register_user(
            email=self.success_user["email"], password=self.success_user["password"]
        )
        self.user_obj.activate()

        self.application_obj = ApplicationModel.objects.create(user=self.user_obj)

    def test_methods(self):
        self.create_document()
        self.delete_document()

    def create_document(self):
        data = {
            "curriculum_vitae": self._create_image(),
            "personal_photo": self._create_image(),
            "valid_passport": self._create_image(),
            "high_school_certificate": self._create_image(),
            "trans_script_high_school_certificate": self._create_image(),
            "bachelor_degree": self._create_image(),
            "trans_script_bachelor_degree": self._create_image(),
            "master_degree": self._create_image(),
            "trans_script_master_degree": self._create_image(),
            "supporting_letter": self._create_image(),
        }
        sql_count = DocumentModel.objects.all().count()
        self.assertEqual(sql_count, 0)
        self.success_document_obj = DocumentModel.objects.create(
            application=self.application_obj, **data
        )
        self.assertIsNotNone(self.success_document_obj)
        self.assertEqual(
            self.success_document_obj.application.user.email, self.user_obj.email
        )
        self.assertEqual(
            self.success_document_obj.application.tracking_id,
            self.application_obj.tracking_id,
        )
        self.assertEqual(
            self.success_document_obj.get_field_file_name("curriculum_vitae"),
            data["curriculum_vitae"].name,
        )
        self.assertEqual(
            self.success_document_obj.get_field_file_name("valid_passport"),
            data["valid_passport"].name,
        )
        self.assertEqual(
            self.success_document_obj.get_field_file_name(
                "trans_script_high_school_certificate"
            ),
            data["trans_script_high_school_certificate"].name,
        )
        self.assertEqual(
            self.success_document_obj.get_field_file_name(
                "trans_script_bachelor_degree"
            ),
            data["trans_script_bachelor_degree"].name,
        )
        self.assertEqual(
            self.success_document_obj.get_field_file_name("trans_script_master_degree"),
            data["trans_script_master_degree"].name,
        )

        directory_path = os.path.join(
            BASE_DIR,
            f"media/application_documents/user_{self.user_obj.email}/{self.application_obj.tracking_id}/",
        )

        self.assertEqual(
            self.success_document_obj.curriculum_vitae.path,
            f'{directory_path}{self.success_document_obj.get_field_file_name("curriculum_vitae")}',
        )
        self.assertTrue(os.path.isfile(self.success_document_obj.curriculum_vitae.path))

        self.assertEqual(
            self.success_document_obj.personal_photo.path,
            f'{directory_path}{self.success_document_obj.get_field_file_name("personal_photo")}',
        )
        self.assertTrue(os.path.isfile(self.success_document_obj.personal_photo.path))

        self.assertEqual(
            self.success_document_obj.valid_passport.path,
            f'{directory_path}{self.success_document_obj.get_field_file_name("valid_passport")}',
        )
        self.assertTrue(os.path.isfile(self.success_document_obj.valid_passport.path))

        self.assertEqual(
            self.success_document_obj.high_school_certificate.path,
            f'{directory_path}{self.success_document_obj.get_field_file_name("high_school_certificate")}',
        )
        self.assertTrue(
            os.path.isfile(self.success_document_obj.high_school_certificate.path)
        )

        self.assertEqual(
            self.success_document_obj.trans_script_high_school_certificate.path,
            f'{directory_path}{self.success_document_obj.get_field_file_name("trans_script_high_school_certificate")}',
        )
        self.assertTrue(
            os.path.isfile(
                self.success_document_obj.trans_script_high_school_certificate.path
            )
        )

        self.assertEqual(
            self.success_document_obj.bachelor_degree.path,
            f'{directory_path}{self.success_document_obj.get_field_file_name("bachelor_degree")}',
        )
        self.assertTrue(os.path.isfile(self.success_document_obj.bachelor_degree.path))

        self.assertEqual(
            self.success_document_obj.trans_script_bachelor_degree.path,
            f'{directory_path}{self.success_document_obj.get_field_file_name("trans_script_bachelor_degree")}',
        )
        self.assertTrue(
            os.path.isfile(self.success_document_obj.trans_script_bachelor_degree.path)
        )

        self.assertEqual(
            self.success_document_obj.master_degree.path,
            f'{directory_path}{self.success_document_obj.get_field_file_name("master_degree")}',
        )
        self.assertTrue(os.path.isfile(self.success_document_obj.master_degree.path))

        self.assertEqual(
            self.success_document_obj.trans_script_master_degree.path,
            f'{directory_path}{self.success_document_obj.get_field_file_name("trans_script_master_degree")}',
        )
        self.assertTrue(
            os.path.isfile(self.success_document_obj.trans_script_master_degree.path)
        )

        self.assertEqual(
            self.success_document_obj.supporting_letter.path,
            f'{directory_path}{self.success_document_obj.get_field_file_name("supporting_letter")}',
        )
        self.assertTrue(
            os.path.isfile(self.success_document_obj.supporting_letter.path)
        )

        sql_count = DocumentModel.objects.all().count()
        self.assertEqual(sql_count, 1)

    def delete_document(self):
        self.success_document_obj.delete()
        sql_count = DocumentModel.objects.all().count()
        self.assertEqual(sql_count, 0)
