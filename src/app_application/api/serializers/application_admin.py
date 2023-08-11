from rest_framework import serializers

from app_application.models import ApplicationModel


class AdminApplicationListSerializer(serializers.ModelSerializer):
    degree = serializers.CharField(source="get_degree_display", read_only=True)
    faculty = serializers.CharField(source="get_faculty_display", read_only=True)
    field_of_study = serializers.CharField(source="get_field_of_study_display", read_only=True)
    university_status = serializers.CharField(source="get_university_status_display", read_only=True)
    faculty_status = serializers.CharField(source="get_faculty_status_display", read_only=True)

    user = serializers.SerializerMethodField(
        'get_user'
    )

    class Meta:
        model = ApplicationModel
        fields = (
            "id",
            "tracking_id",

            "degree",
            "faculty",
            "field_of_study",
            "university_status",
            "faculty_status",

            "jalali_created_at",

            "user"
        )

    def get_user(self, obj):
        return {
            "full_name": obj.user.user_profile.get_full_name(),
            "gender": obj.user.user_profile.gender,
            "country": obj.user.user_address.country,
            "age": obj.user.user_profile.get_age()
        }
