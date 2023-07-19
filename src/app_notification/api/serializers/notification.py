from rest_framework import serializers

from app_notification.models import NotificationModel


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationModel
        fields = (
            'id',
            'title',
            'message',
            'view_status',
            'status',
        )
