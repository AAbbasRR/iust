from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from utils import GeneralEducationModel, GeneralDateModel

UserModel = get_user_model()


class HighSchool(GeneralEducationModel, GeneralDateModel):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name="user_high_school",
        verbose_name=_('User')
    )
