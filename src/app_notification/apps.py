from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppNotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_notification'
    verbose_name = _("App Notification")
    verbose_name_plural = _("App Notifications")
