from django.db import models
from django.utils.translation import gettext_lazy as _

from app_user.models import UserModel

from utils.general_models import GeneralDateModel


class NotificationManager(models.Manager):
    pass


class Notification(GeneralDateModel):
    class NotificationStatusOptions(models.TextChoices):
        Information = "Information", _("Information")
        Success = "Success", _("Success")
        Warning = "Warning", _("Warning")
        Error = "Error", _("Error")

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="user_notifications",
        verbose_name=_("User"),
    )
    title = models.CharField(max_length=75, verbose_name=_("Title"))
    message = models.TextField(verbose_name=_("Message"))
    view_status = models.BooleanField(default=False, verbose_name=_("View Status"))
    status = models.CharField(
        max_length=11,
        choices=NotificationStatusOptions.choices,
        default=NotificationStatusOptions.Information,
        verbose_name=_("Status"),
    )

    objects = NotificationManager()

    def view_message(self):
        self.view_status = True
        self.save()
