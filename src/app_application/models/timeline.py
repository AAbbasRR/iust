from django.db import models
from django.utils.translation import gettext as _

from app_application.models import ApplicationModel
from app_user.models import UserModel

from utils.general_models import GeneralDateModel
from utils.data_list import application_timeline_status_options


class TimeLineManager(models.Manager):
    pass


class TimeLine(GeneralDateModel):
    application = models.ForeignKey(
        ApplicationModel,
        on_delete=models.CASCADE,
        related_name="application_timeline",
        verbose_name=_("Application")
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="user_timeline",
        verbose_name=_("User")
    )
    status = models.CharField(
        max_length=4,
        choices=application_timeline_status_options,
        verbose_name=_("Status")
    )
    title = models.CharField(
        max_length=20,
        verbose_name=_("Title")
    )
    message = models.TextField(
        verbose_name=_("Message")
    )

    objects = TimeLineManager()
