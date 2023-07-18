from django.db import models
from django.utils.translation import gettext as _

from app_user.models import UserModel

from utils import GeneralDateModel
from utils.data_list import application_status_options

import uuid


class ApplicationManager(models.Manager):
    def find_with_tracking_id(self, tracking_id):
        return self.filter(tracking_id=tracking_id).first()


class Application(GeneralDateModel):
    class Meta:
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")
        ordering = ['-id']

    user = models.ForeignKey(
        UserModel,
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
        null=True,
        verbose_name=_('Full Name')
    )
    comments = models.TextField(
        null=True,
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

    objects = ApplicationManager()

    def __str__(self):
        return self.tracking_id
