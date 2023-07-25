from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _

from Abrat.settings import (
    DATE_INPUT_FORMATS,
    TIME_INPUT_FORMATS
)


class GeneralDateModel(models.Model):
    create_at = models.DateTimeField(
        verbose_name=_('Created Time'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated Time'),
        auto_now=True
    )

    def created_at(self):
        return self.create_at.strftime(f'{DATE_INPUT_FORMATS} - {TIME_INPUT_FORMATS}')

    class Meta:
        abstract = True


class GeneralAddressModel(models.Model):
    country = models.CharField(
        max_length=35,
        verbose_name=_('Country'),
    )
    city = models.CharField(
        max_length=40,
        verbose_name=_('City'),
    )

    class Meta:
        abstract = True


class GeneralEducationModel(GeneralAddressModel):
    date_of_graduation = models.DateField(
        verbose_name=_('Date Of Graduation'),
        auto_now=False,
        auto_now_add=False,
    )
    gpa = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name=_('GPA'),
    )
    field_of_study = models.CharField(
        verbose_name=_('Field Of Study'),
        max_length=50,
    )

    class Meta:
        abstract = True
