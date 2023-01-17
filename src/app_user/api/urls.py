from django.urls import path

from .views import *

app_name = 'app_user'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('register/active_account/', UserVerifyRegisterView.as_view(), name='user_active_account'),
    path('register/resent_activate_code/', UserReSendRegisterOTPCodeView.as_view(), name='user_resent_active_code'),

    path('login/', UserLoginView.as_view(), name='user_login'),
]
