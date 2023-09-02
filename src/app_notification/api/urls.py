from django.urls import path

from .views import *

app_name = 'app_notification'
urlpatterns = [
    path('list/', ListNotificationView.as_view(), name='user_list_notification'),
    path('view/', ViewNotificationView.as_view(), name='user_view_notification'),
]
