from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

from utils import ManageMailService, RedisKeys

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_handler(sender, instance, **kwargs):
    if kwargs['created']:
        Token.objects.create(
            user=instance
        )
        if instance.is_active is False:
            manage_email_obj = ManageMailService(instance.email)
            manage_email_obj.send_otp_code(RedisKeys.activate_account)
