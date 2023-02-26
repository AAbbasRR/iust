from django.db import models
from django.utils.translation import gettext as _

from app_application.models import ApplicationModel

from utils import GeneralDateModel
from utils.data_list import occupation_options


class LatestOccupationManager(models.Manager):
    pass


class LatestOccupation(GeneralDateModel):
    application = models.OneToOneField(
        ApplicationModel,
        on_delete=models.CASCADE,
        verbose_name=_('Application')
    )
    occupation = models.CharField(
        max_length=3,
        choices=occupation_options,
        verbose_name=_('Occupation')
    )
    organization = models.CharField(
        max_length=50,
        verbose_name=_('Organization')
    )
    from_date = models.DateField(
        verbose_name=_('From Date')
    )
    to_date = models.DateField(
        verbose_name=_('To Date')
    )
    description = models.TextField(
        verbose_name=_('Description')
    )

    objects = LatestOccupationManager()