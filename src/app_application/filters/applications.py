from django.db.models import Count, F

from django_filters import (
    FilterSet,
    CharFilter,
    BooleanFilter,
    RangeFilter,
    DateTimeFromToRangeFilter,
)

from app_application.models import ApplicationModel
from app_user.models import UserModel


class ApplicationListFilter(FilterSet):
    age = RangeFilter(field_name="user__user_profile__age")
    country = CharFilter(
        field_name="user__user_address__country", lookup_expr="contains"
    )
    agent = CharFilter(field_name="agent__email", lookup_expr="contains")
    gender = CharFilter(field_name="user__user_profile__gender")
    more_than_one_request = BooleanFilter(method="get_more_than_one_request")
    create_at = DateTimeFromToRangeFilter(field_name="create_at")

    class Meta:
        model = ApplicationModel
        fields = [
            "age",
            "status",
            "degree",
            "faculty",
            "field_of_study",
            "country",
            "agent",
            "gender",
            "more_than_one_request",
            "create_at",
        ]

    def get_more_than_one_request(self, queryset, name, value):
        users_with_count = UserModel.objects.annotate(
            application_count=Count("user_application")
        )
        users_with_multiple_applications = users_with_count.filter(
            application_count__gt=1
        )
        return queryset.filter(user__in=users_with_multiple_applications)
