from django.db import models
from django.utils.translation import gettext as _

from app_user.models import UserModel

from utils import GeneralAddressModel, GeneralDateModel


class AddressManager(models.Manager):
    pass


class Address(GeneralDateModel, GeneralAddressModel):
    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
        ordering = ['-id']

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name="user_address",
        verbose_name=_('User')
    )
    country_code = models.CharField(
        max_length=5,
        null=True,
        verbose_name=_('Country Code')
    )
    postal_code = models.CharField(
        max_length=20,
        verbose_name=_('Postal Code')
    )
    city_code = models.CharField(
        max_length=5,
        null=True,
        verbose_name=_('City Code')
    )
    phone_number = models.CharField(
        max_length=25,
        null=True,
        verbose_name=_('Phone Number')
    )
    address = models.TextField(
        verbose_name=_('Address')
    )

    objects = AddressManager()

    def __str__(self):
        return self.user.email
