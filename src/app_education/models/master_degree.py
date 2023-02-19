from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from utils import GeneralEducationModel, GeneralDateModel

User = get_user_model()


class MasterDegree(GeneralEducationModel, GeneralDateModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_master_degree",
        verbose_name=_('User')
    )
    university = models.CharField(
        max_length=50,
        verbose_name=_('University')
    )
