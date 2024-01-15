from django.db import models
from django.utils.translation import gettext_lazy as _

from app_application.models import ApplicationModel
from app_user.models import UserModel

from utils.general_models import GeneralDateModel


class TimeLineManager(models.Manager):
    pass


class TimeLine(GeneralDateModel):
    class TimeLineStatusOptions(models.TextChoices):
        Confirmation = "Confirmation", _("Confirmation")
        Rejection = "Rejection", _("Rejection")
        Investigation = "Investigation", _("Investigation")
        Referral = "Referral", _("Referral")
        NeedToEdit = "NeedToEdit", _("Need To Edit")

    application = models.ForeignKey(
        ApplicationModel,
        on_delete=models.CASCADE,
        related_name="application_timeline",
        verbose_name=_("Application"),
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="user_timeline",
        verbose_name=_("User"),
    )
    status = models.CharField(
        max_length=13,
        choices=TimeLineStatusOptions.choices,
        default=TimeLineStatusOptions.Investigation,
        verbose_name=_("Status"),
    )
    message = models.TextField(verbose_name=_("Message"))

    objects = TimeLineManager()
