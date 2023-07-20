from django.utils.translation import gettext as _

from rest_framework import (
    serializers,
    exceptions
)

from app_chat.models import (
    ChatRoomModel,
    MessageModel,
)

from utils.base_errors import BaseErrors


class MessageSerializers(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField(
        'get_file_url'
    )
    user_owner = serializers.SerializerMethodField(
        'get_user_owner'
    )

    chatroom_id = serializers.CharField(
        required=True,
        write_only=True
    )

    class Meta:
        model = MessageModel
        fields = [
            'id',
            'message',
            'create_at',

            'file_url',
            'user_owner',

            'file',
            'chatroom_id',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'message': {'required': True},
            'file': {'required': False, 'write_only': True},
        }

    def __init__(self, *args, **kwargs):
        super(MessageSerializers, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user

    def validate_chatroom_id(self, value):
        chatroom_obj = ChatRoomModel.objects.filter(pk=value, user=self.user).first()
        if chatroom_obj:
            return chatroom_obj
        else:
            raise exceptions.NotFound(BaseErrors._change_error_variable('object_not_found', object=_('Chat Room')))

    def get_file_url(self, obj):
        return obj.get_file_url(self.request)

    def get_user_owner(self, obj):
        return True if self.user == obj.user else False

    def create(self, validated_data):
        chat_room_obj = validated_data.pop('chatroom_id')
        message_obj = MessageModel.objects.create(
            chat_room=chat_room_obj,
            user=self.user,
            **validated_data
        )
        chat_room_obj.status = 'AWF'
        chat_room_obj.save()
        return message_obj


class TicketChatRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChatRoomModel
        fields = [
            'id',
            'title',
            'room_id',
            'status',
            'priority',
            'create_at',
            'update_at',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'title': {'required': True},
            'priority': {'required': True},
            'status': {'read_only': True},
            'room_id': {'read_only': True},
            'create_at': {'read_only': True},
            'update_at': {'read_only': True},
        }

    def __init__(self, *args, **kwargs):
        super(TicketChatRoomSerializers, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user

    def create(self, validated_data):
        chatroom_obj = ChatRoomModel.objects.create(
            user=self.user,
            **validated_data
        )
        return chatroom_obj


class ChatRoomRetrieveSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField(
        'get_messages'
    )

    class Meta:
        model = ChatRoomModel
        fields = [
            'id',
            'title',
            'room_id',
            'status',
            'priority',
            'create_at',

            'messages',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'title': {'read_only': True},
            'room_id': {'read_only': True},
            'status': {'read_only': True},
            'priority': {'read_only': True},
            'create_at': {'read_only': True},
        }

    def get_messages(self, obj):
        return MessageSerializers(obj.chatroom_messages.all().order_by('create_at'), many=True, context=self.context).data