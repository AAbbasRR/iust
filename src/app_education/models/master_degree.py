from django.db import models
from django.utils.translation import gettext as _

from app_user.models import UserModel

from utils import GeneralEducationModel, GeneralDateModel


class MasterDegree(GeneralEducationModel, GeneralDateModel):
    class Meta:
        verbose_name = _("MasterDegree")
        verbose_name_plural = _("Master Degrees")
        ordering = ["-id"]

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name="user_master_degree",
        verbose_name=_("User"),
    )
    university = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("University")
    )
