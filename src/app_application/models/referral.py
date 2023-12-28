from django.db import models
from django.utils.translation import gettext as _

from app_application.models import ApplicationModel
from app_user.models import UserModel

from utils.general_models import GeneralDateModel


class TimeLineManager(models.Manager):
    pass


class Referral(GeneralDateModel):
    application = models.ForeignKey(
        ApplicationModel,
        on_delete=models.CASCADE,
        related_name="application_referral",
        verbose_name=_("Application"),
    )
    origin_user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="origin_user_referral",
        verbose_name=_("Origin User"),
    )
    destination_user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="destination_user_referral",
        verbose_name=_("Destination User"),
    )
    is_enabled = models.BooleanField(
        default=True,
        verbose_name=_("Is Enabled"),
    )

    objects = TimeLineManager()
