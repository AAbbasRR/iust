from rest_framework import (
    serializers,
    exceptions
)

from app_application.models import (
    TimeLineModel,
    ApplicationModel
)

from utils.base_errors import BaseErrors


class AdminApplicationTimeLineSerializer(serializers.ModelSerializer):
    application = serializers.IntegerField(
        required=True,
        write_only=True
    )

    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model = TimeLineModel
        fields = (
            "id",

            "status",
            "title",
            "message",

            "application",

            "jalali_created_at"
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'jalali_created_at': {'read_only': True},
        }

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.request = self.context.get('request')
        if self.request:
            self.user = self.request.user

    def validate_application(self, value):
        application_obj = ApplicationModel.objects.filter(pk=value).first()
        if application_obj is not None:
            return application_obj
        else:
            raise exceptions.NotFound(BaseErrors.tracking_id_not_found)

    def create(self, validated_data):
        TimeLineModel.objects.create(
            user=self.user,
            **validated_data
        )
