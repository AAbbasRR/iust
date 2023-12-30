from .register import (
    UserRegisterView,
    UserVerifyRegisterView,
    UserReSendRegisterOTPCodeView,
)
from .login import UserLoginView
from .forget_password import (
    ForgetPasswordView,
    ValidateForgetPasswordOTPView,
    CompleteForgetPasswordView,
)
from .change_password import ChangePasswordView
from .profile import ProfileDetailUpdateView
from .address import AddressDetailUpdateView
from .user import UserProfileDetailView
from .admin_detail import AdminDetailDataView
