from django.urls import path

from .views import *

app_name = 'app_user'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('register/active_account/', UserVerifyRegisterView.as_view(), name='user_active_account'),
    path('register/resent_activate_code/', UserReSendRegisterOTPCodeView.as_view(), name='user_resent_active_code'),

    path('login/', UserLoginView.as_view(), name='user_login'),

    path('forget_password/', ForgetPasswordView.as_view(), name='user_forget_password'),
    path('forget_password/validate/', ValidateForgetPasswordOTPView.as_view(), name='user_validate_forget_password'),
    path('forget_password/complete/', CompleteForgetPasswordView.as_view(), name='user_complete_forget_password'),

    path('profile/create/', ProfileCreateView.as_view(), name='user_create_profile'),
    path('profile/detail_update/', ProfileDetailUpdateView.as_view(), name='user_detail_update_profile'),
]
