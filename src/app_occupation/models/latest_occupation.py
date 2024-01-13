from django.db import models
from django.utils.translation import gettext_lazy as _

from app_user.models import UserModel

from utils import GeneralDateModel, GeneralAddressModel


class LatestOccupationManager(models.Manager):
    pass


class LatestOccupation(GeneralDateModel, GeneralAddressModel):
    class Meta:
        verbose_name = _("Latest Occupation")
        verbose_name_plural = _("Latest Occupations")
        ordering = ["-id"]

    class LatestOccupationOptions(models.TextChoices):
        Other = "Other", _("Other")
        Academician = "Academician", _("Academician")
        Government_Employee = "Government_Employee", _("Government Employee")
        Industrial_Employee = "Industrial_Employee", _("Industrial Employee")
        Student = "Student", _("Student")

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name="user_latest_occupation",
        verbose_name=_("User"),
    )
    occupation = models.CharField(
        max_length=19,
        choices=LatestOccupationOptions.choices,
        default=LatestOccupationOptions.Other,
        verbose_name=_("Occupation"),
    )
    organization = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Organization")
    )
    from_date = models.DateField(null=True, blank=True, verbose_name=_("From Date"))
    to_date = models.DateField(null=True, blank=True, verbose_name=_("To Date"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))

    objects = LatestOccupationManager()
