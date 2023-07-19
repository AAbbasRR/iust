from django.db import models
from django.utils.translation import gettext as _

from app_user.models import UserModel

from utils.general_models import GeneralDateModel
from utils.data_list import notification_status_options


class NotificationManager(models.Manager):
    pass


class Notification(GeneralDateModel):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        verbose_name=_('User')
    )
    title = models.CharField(
        max_length=75,
        verbose_name=_('Title')
    )
    message = models.TextField(
        verbose_name=_('Message')
    )
    view_status = models.BooleanField(
        default=False,
        verbose_name=_('View Status')
    )
    status = models.CharField(
        max_length=4,
        choices=notification_status_options,
        default=notification_status_options[0][0],
        verbose_name=_('Status')
    )

    objects = NotificationManager()

    def view_message(self):
        self.view_status = True
        self.save()
