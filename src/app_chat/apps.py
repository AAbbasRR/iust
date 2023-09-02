from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_chat'
    verbose_name = _("App Chat")
    verbose_name_plural = _("App Chat")

    def ready(self):
        import utils.signals.chat
