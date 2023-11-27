from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppOccupationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_occupation"
    verbose_name = _("App Occupation")
    verbose_name_plural = _("App Occupations")
