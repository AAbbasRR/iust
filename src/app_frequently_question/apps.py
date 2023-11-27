from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppFrequentlyQuestionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_frequently_question"
    verbose_name = _("App Frequently Question")
    verbose_name_plural = _("App Frequently Questions")
