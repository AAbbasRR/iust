from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class AdminManager(models.Manager):
    pass


class Admin(models.Model):
    class AdminRoleOptions(models.TextChoices):
        faculty_director = "faculty_director", _("Faculty Director")
        department_head = "department_head", _("Department Head")
        department_member = "department_member", _("Department Member")

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="user_admin",
        verbose_name=_("User"),
    )
    role = models.CharField(
        max_length=17,
        choices=AdminRoleOptions.choices,
        default=AdminRoleOptions.department_member,
        verbose_name=_("Role"),
    )
    schools = models.CharField(max_length=128, verbose_name=_("Schools"))
    fields = models.CharField(
        max_length=128, null=True, blank=True, verbose_name=_("Fields")
    )

    objects = AdminManager()
