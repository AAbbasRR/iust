from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_application'
    verbose_name = _("App Application")
    verbose_name_plural = _("App Applications")

    def ready(self):
        import utils.signals.documents
        import utils.signals.application
