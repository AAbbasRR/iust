from django.test import Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APITestCase

from faker import Faker
from PIL import Image
import io


class TestApplicationSetUp(APITestCase):
    def setUp(self):
        self.client = Client()

        self.fake_data = Faker()

        self.list_all_user_application_api = reverse('app_application:application_all_list', kwargs={"version": "v1"})
        self.create_application_api = reverse('app_application:application_create', kwargs={"version": "v1"})

        self.create_document_api = reverse('app_application:application_create_document', kwargs={"version": "v1"})

        super(TestApplicationSetUp, self).setUp()

    def _detail_update_application_api(self, tracking_id):
        return reverse('app_application:application_detail_update', kwargs={"version": "v1", "tracking_id": tracking_id})

    def _detail_update_document_api(self, application_tracking_id):
        return reverse('app_application:application_detail_update_document', kwargs={"version": "v1", "tracking_id": application_tracking_id})

    def _create_image(self):
        image = Image.new('RGB', (200, 200), color=self.fake_data.hex_color())

        image_io = io.BytesIO()
        image_format = self.fake_data.random_choices(['png', 'jpeg'], 1)[0]
        image.save(image_io, format=image_format)
        image_io.seek(0)

        image_file = SimpleUploadedFile(self.fake_data.file_name(extension=image_format), image_io.read(), content_type="image/jpeg")
        return image_file

    def tearDown(self):
        super(TestApplicationSetUp, self).tearDown()
