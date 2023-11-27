from django.utils.translation import gettext as _


class BaseErrors:
    @classmethod
    def _change_error_variable(cls, error_name, **kwargs):
        message = getattr(cls, error_name)
        for key, value in kwargs.items():
            message = message.replace("{%s}" % key, value)
        return message

    # global
    parameter_is_required = _("parameter {param_name} is required")
    object_not_found = _("{object} Not Found")
    invalid_access_token = _("Invalid Access Token Or Expired")

    # project
    url_not_found = _("URL Not Found.")
    server_error = _("Server Error.")

    # user sign up, login, forget pass, change pass
    # sign up
    user_must_have_email = _("User Must Have Email.")
    user_must_have_password = _("User Must Have Password.")
    user_account_with_email_exists = _("User Account With Email Exists.")
    # active account
    user_account_is_active = _("User Account Is Active.")
    # login
    invalid_email_or_password = _("Invalid Email or Password.")
    user_account_not_active = _("User Account Not Active.")
    # forget pass
    user_not_found = _("User Not Found")
    user_dont_have_forget_password_permission = _(
        "You Do Not Have Access To Change The Password, Please Try Again First Step."
    )
    passwords_did_not_match = _("Password And Repeat Password Did Not Match.")
    # change pass
    old_password_is_incorrect = _("Old Password Is Incorrect")

    # otp code validate
    otp_code_expired = _("OTP Code Expired, Please Try To Resend New OTP Code.")
    invalid_otp_code = _("Invalid OTP Code, Please Try Again.")
    otp_code_has_already_been_sent = _("OTP Code Has Already Been Sent.")

    # api serializer
    tracking_id_not_found = _('"tracking_id" Not Found Or Is Invalid')
    invalid_choice_value = _('"{input}" is not a valid choice.')

    invalid_file_formats = _('Only "{formats}" formats are allowed.')
    invalid_file_size = _('Image size should not exceed "{size}" bytes.')
    invalid_upload_file = _("Invalid file. Please upload a valid file.")

    # admin
    user_is_not_admin = _("User Is Not Admin")

    # notification
    message_success_viewed = _("Message Success Viewed")

    # api views
