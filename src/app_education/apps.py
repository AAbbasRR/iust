from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppEducationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_education"
    verbose_name = _("App Education")
    verbose_name_plural = _("App Educations")
