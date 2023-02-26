from django.test import Client
from django.urls import reverse

from rest_framework.test import APITestCase


class TestUserSetUp(APITestCase):
    def setUp(self):
        self.client = Client()
        self.register_api = reverse('app_user:user_register', kwargs={"version": "v1"})
        self.active_account_api = reverse('app_user:user_active_account', kwargs={"version": "v1"})
        self.resend_activation_otp_api = reverse('app_user:user_resent_active_code', kwargs={"version": "v1"})
        self.login_api = reverse('app_user:user_login', kwargs={"version": "v1"})
        self.forget_password_api = reverse('app_user:user_forget_password', kwargs={"version": "v1"})
        self.validate_forget_password_api = reverse('app_user:user_validate_forget_password', kwargs={"version": "v1"})
        self.complete_forget_password_api = reverse('app_user:user_complete_forget_password', kwargs={"version": "v1"})
        self.create_profile_api = reverse('app_user:user_create_profile', kwargs={"version": "v1"})
        self.detail_update_profile_api = reverse('app_user:user_detail_update_profile', kwargs={"version": "v1"})
        self.create_address_api = reverse('app_user:user_create_address', kwargs={"version": "v1"})
        self.detail_update_address_api = reverse('app_user:user_detail_update_address', kwargs={"version": "v1"})

        super(TestUserSetUp, self).setUp()

    def tearDown(self):
        super(TestUserSetUp, self).tearDown()
