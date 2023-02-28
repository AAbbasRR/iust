from django.contrib.auth import get_user_model

from app_application.models import ApplicationModel, DocumentModel
from app_application.tests import TestApplicationSetUp

UserModel = get_user_model()


class DocumentTestCase(TestApplicationSetUp):
    def setUp(self):
        super(DocumentTestCase, self).setUp()

        self.success_user = {
            "email": "mail@mail.com",
            "password": "a1A23456",
        }
        self.user_obj = UserModel.objects.register_user(
            email=self.success_user['email'],
            password=self.success_user['password']
        )
        self.user_obj.activate()

        self.application_obj = ApplicationModel.objects.create(
            user=self.user_obj
        )

    def test_methods(self):
        self.create_document()
        self.delete_document()

    def create_document(self):
        data = {
            'curriculum_vitae': self.fake_data.file_name(),
            'personal_photo': self.fake_data.file_name(),
            'valid_passport': self.fake_data.file_name(),
            'high_school_certificate': self.fake_data.file_name(),
            'trans_script_high_school_certificate': self.fake_data.file_name(),
            'bachelor_degree': self.fake_data.file_name(),
            'trans_script_bachelor_degree': self.fake_data.file_name(),
            'master_degree': self.fake_data.file_name(),
            'trans_script_master_degree': self.fake_data.file_name(),
            'supporting_letter': self.fake_data.file_name(),
        }
        sql_count = DocumentModel.objects.all().count()
        self.assertEqual(sql_count, 0)
        self.success_document_obj = DocumentModel.objects.create(
            application=self.application_obj,
            **data
        )
        self.assertIsNotNone(self.success_document_obj)
        self.assertEqual(self.success_document_obj.application.user.email, self.user_obj.email)
        self.assertEqual(self.success_document_obj.application.tracking_id, self.application_obj.tracking_id)
        self.assertEqual(self.success_document_obj.curriculum_vitae, data['curriculum_vitae'])
        self.assertEqual(self.success_document_obj.high_school_certificate, data['high_school_certificate'])
        self.assertEqual(self.success_document_obj.trans_script_bachelor_degree, data['trans_script_bachelor_degree'])
        self.assertEqual(self.success_document_obj.supporting_letter, data['supporting_letter'])

        sql_count = DocumentModel.objects.all().count()
        self.assertEqual(sql_count, 1)

    def delete_document(self):
        self.success_document_obj.delete()
        sql_count = DocumentModel.objects.all().count()
        self.assertEqual(sql_count, 0)
