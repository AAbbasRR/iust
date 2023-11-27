from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.utils import IntegrityError

from app_chat.models import ChatRoomModel

import uuid


@receiver(post_save, sender=ChatRoomModel)
def create_product_inventory_handler(sender, instance, **kwargs):
    if kwargs["created"]:
        while True:
            try:
                instance.room_id = str(uuid.uuid4()).split("-")[-1]
                instance.save()
                break
            except IntegrityError:
                pass
