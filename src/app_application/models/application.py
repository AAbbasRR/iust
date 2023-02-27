from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from utils import GeneralDateModel
from utils.data_list import application_status_options

import uuid

User = get_user_model()


class Application(GeneralDateModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_application",
        verbose_name=_('User')
    )
    tracking_id = models.CharField(
        max_length=12,
        default=str(uuid.uuid4()).split('-')[-1],
        unique=True,
        null=False,
        blank=False,
        verbose_name=_('Tracking ID')
    )
    full_name = models.CharField(
        max_length=50,
        verbose_name=_('Full Name')
    )
    comments = models.TextField(
        verbose_name=_('Comments')
    )
    applied_program = models.BooleanField(
        default=False,
        verbose_name=_('Applied Program')
    )
    financial_self_support = models.BooleanField(
        default=True,
        verbose_name=_('Financial Self Support')
    )
    status = models.CharField(
        max_length=4,
        choices=application_status_options,
        default=application_status_options[0][0],
        verbose_name=_('Status')
    )
