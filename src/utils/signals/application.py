from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError

from app_application.models import ApplicationModel

import uuid


@receiver(post_save, sender=ApplicationModel)
def create_application_handler(sender, instance, **kwargs):
    if kwargs["created"]:
        while True:
            try:
                instance.tracking_id = str(uuid.uuid4()).split("-")[-1]
                instance.save()
                break
            except IntegrityError:
                pass
