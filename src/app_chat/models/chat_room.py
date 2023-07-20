from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

from Abrat.settings import DEBUG
from app_user.models import UserModel

from utils.general_models import GeneralDateModel
from utils.data_list import (
    ticket_status_choices,
    ticket_priority_choices
)


class ChatRoomManager(models.Manager):
    pass


class ChatRoom(GeneralDateModel):
    title = models.CharField(
        max_length=75,
        verbose_name=_('Title')
    )
    is_group = models.BooleanField(
        default=False,
        verbose_name=_('Is Group')
    )
    is_ticket = models.BooleanField(
        default=True,
        verbose_name=_('Is Ticket')
    )
    members = models.ManyToManyField(
        UserModel,
        related_name='user_chat_rooms',
        verbose_name=_('Members')
    )
    room_id = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name=_('Room Id')
    )
    status = models.CharField(
        max_length=5,
        choices=ticket_status_choices,
        default=ticket_status_choices[0][0],
        verbose_name=_('Status')
    )
    priority = models.CharField(
        max_length=3,
        choices=ticket_priority_choices,
        default=ticket_priority_choices[0][0],
        verbose_name=_('Priority')
    )

    objects = ChatRoomManager()


def ticket_image_directory_path(instance, filename):
    return 'chat_images/{0}/{1}'.format(instance.message.chat_room.room_id, filename)


class Message(GeneralDateModel):
    chat_room = models.ForeignKey(
        ChatRoom,
        on_delete=models.CASCADE,
        related_name='chatroom_messages',
        verbose_name=_('Chat Room')
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='user_messages',
        verbose_name=_('User')
    )
    message = models.TextField(
        verbose_name=_('Message')
    )
    file = models.FileField(
        upload_to=ticket_image_directory_path,
        verbose_name=_('Image')
    )

    def get_file_url(self, request):
        if self.file is None or self.file == "":
            return None
        else:
            host = request.get_host()
            protocol = request.build_absolute_uri().split(host)[0]
            protocol = protocol if DEBUG else protocol.replace("http", "https") if protocol.split(":")[0] == "http" else protocol
            website_url = protocol + host
            return website_url + self.file.url
