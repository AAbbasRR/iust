from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_user'
    verbose_name = _("App User")
    verbose_name_plural = _("App Users")

    def ready(self):
        import utils.signals.user
