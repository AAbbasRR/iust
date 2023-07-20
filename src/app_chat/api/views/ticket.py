from django.utils.translation import gettext as _

from rest_framework import (
    generics,
    exceptions,
    response,
    status
)

from app_chat.api.serializers.ticket import (
    TicketChatRoomSerializers,
    MessageSerializers,
    ChatRoomRetrieveSerializer
)
from app_chat.models import ChatRoomModel

from utils.permissions import IsAuthenticatedPermission
from utils.base_errors import BaseErrors
from utils.versioning import BaseVersioning
from utils.paginations import BasePagination


class ListCreateTicketView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = TicketChatRoomSerializers

    def get_queryset(self):
        return ChatRoomModel.objects.filter(user=self.request.user)


class RetrieveTicketMessagesView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedPermission]
    versioning_class = BaseVersioning
    serializer_class = ChatRoomRetrieveSerializer
    lookup_field = 'pk'

    def get_object(self):
        pk_param_value = self.request.GET.get(self.lookup_field, None)
        if pk_param_value is None or pk_param_value == '':
            raise exceptions.ParseError(BaseErrors._change_error_variable('parameter_is_required', param_name='pk'))
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.filter(pk=pk_param_value).first()
        if obj is None:
            raise exceptions.NotFound(BaseErrors._change_error_variable('object_not_found', object=_('Ticket')))
        return obj

    def get_queryset(self):
        return ChatRoomModel.objects.filter(user=self.request.user)


class CreateMessageOnChatRoomView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedPermission]
    versioning_class = BaseVersioning
    serializer_class = MessageSerializers

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            message = serializer.save()
            return response.Response(
                MessageSerializers(instance=message, many=False, context={'request': request}).data,
                status=status.HTTP_201_CREATED
            )
