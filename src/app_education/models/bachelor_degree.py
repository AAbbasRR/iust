from django.db import models
from django.utils.translation import gettext as _

from app_user.models import UserModel

from utils import GeneralEducationModel, GeneralDateModel


class BachelorDegree(GeneralEducationModel, GeneralDateModel):
    class Meta:
        verbose_name = _("Bachelor Degree")
        verbose_name_plural = _("Bachelor Degrees")
        ordering = ['-id']

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name="user_bachelor_degree",
        verbose_name=_('User')
    )
    university = models.CharField(
        max_length=50,
        verbose_name=_('University')
    )
