from django.db import models
from django.utils.translation import gettext as _

from .data_list import country


class GeneralDateModel(models.Model):
    create_at = models.DateTimeField(
        verbose_name=_('Created Time'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated Time'),
        auto_now=True
    )

    class Meta:
        abstract = True


class GeneralAddressModel(models.Model):
    country = models.CharField(
        verbose_name=_('Country'),
        max_length=35,
        choices=country,
    )
    city = models.CharField(
        verbose_name=_('City'),
        max_length=40,
    )

    class Meta:
        abstract = True


class GeneralEducationModel(models.Model):
    date_of_graduation = models.DateField(
        verbose_name=_('Date Of Graduation'),
        auto_now=False,
        auto_now_add=False,
    )
    gpa = models.CharField(
        verbose_name=_('GPA'),
        max_length=40,
    )
    field_of_study = models.CharField(
        verbose_name=_('Field Of Study'),
        max_length=50,
    )

    class Meta:
        abstract = True
