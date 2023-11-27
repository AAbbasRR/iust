from django.db import models
from django.utils.translation import gettext as _

from app_user.models import UserModel

from utils import GeneralDateModel, GeneralAddressModel
from utils.data_list import occupation_options


class LatestOccupationManager(models.Manager):
    pass


class LatestOccupation(GeneralDateModel, GeneralAddressModel):
    class Meta:
        verbose_name = _("Latest Occupation")
        verbose_name_plural = _("Latest Occupations")
        ordering = ["-id"]

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name="user_latest_occupation",
        verbose_name=_("User"),
    )
    occupation = models.CharField(
        max_length=3,
        choices=occupation_options,
        default=occupation_options[0][0],
        verbose_name=_("Occupation"),
    )
    organization = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Organization")
    )
    from_date = models.DateField(null=True, blank=True, verbose_name=_("From Date"))
    to_date = models.DateField(null=True, blank=True, verbose_name=_("To Date"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))

    objects = LatestOccupationManager()
