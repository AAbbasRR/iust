from django.db import models
from django.utils.translation import gettext_lazy as _

from app_user.models import UserModel

from utils import GeneralEducationModel, GeneralDateModel


class HighSchool(GeneralEducationModel, GeneralDateModel):
    class Meta:
        verbose_name = _("High School")
        verbose_name_plural = _("High Schools")
        ordering = ["-id"]

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name="user_high_school",
        verbose_name=_("User"),
    )
