from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class AdminManager(models.Manager):
    pass


class Admin(models.Model):
    class AdminRoleOptions(models.TextChoices):
        staff = "staff"
        prof = "prof"
        karshenas = "karshenas"

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name="user_admin",
        verbose_name=_("User"),
    )
    role = models.CharField(
        max_length=9,
        choices=AdminRoleOptions.choices,
        default=AdminRoleOptions.staff,
        verbose_name=_("Role"),
    )

    objects = AdminManager()
