from django.urls import path

from .views import *

app_name = "app_chat"
urlpatterns = [
    # user tickets
    path(
        "list_create/",
        ListCreateTicketView.as_view(),
        name="user_list_create_ticket_chatroom",
    ),
    path(
        "retrieve/",
        RetrieveTicketMessagesView.as_view(),
        name="user_retrieve_ticket_chatroom",
    ),
    path(
        "message/create/",
        CreateMessageOnChatRoomView.as_view(),
        name="user_create_message_chatroom",
    ),
]
