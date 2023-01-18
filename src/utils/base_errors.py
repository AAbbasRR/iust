from django.utils.translation import gettext as _


class BaseErrors:
    url_not_found = _('URL Not Found.')
    server_error = _('Server Error.')
    user_must_have_email = _('User Must Have Email.')
    user_must_have_password = _('User Must Have Password.')
    invalid_email_or_password = _('Invalid Email or Password.')
    user_account_with_email_exists = _('User Account With Email Exists.')
    passwords_did_not_match = _('Password And Repeat Password Did Not Match.')
    user_not_found = _('User Not Found')
    otp_code_expired = _('OTP Code Expired, Please Try To Resend New OTP Code.')
    invalid_otp_code = _('Invalid OTP Code, Please Try Again.')
    otp_code_has_already_been_sent = _('OTP Code Has Already Been Sent.')
    user_account_not_active = _('User Account Not Active.')
    user_account_is_active = _('User Account Is Active.')
