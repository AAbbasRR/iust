from django.db.models import (
    Count,
    F
)

from django_filters import (
    FilterSet,
    CharFilter,
    BooleanFilter,
    NumberFilter,
    RangeFilter
)

from app_application.models import ApplicationModel
from app_user.models import UserModel

from datetime import datetime


class ApplicationListFilter(FilterSet):
    country = CharFilter(field_name="user__", lookup_expr='contains')
    agent = CharFilter(field_name="user__agent", lookup_expr='contains')
    gender = CharFilter(field_name="user__user_profile__gender")
    min_age = NumberFilter(method="get_min_age")
    max_age = NumberFilter(method="get_max_age")
    more_than_one_request = BooleanFilter(method="get_more_than_one_request")
    create_at = RangeFilter("create_at")

    class Meta:
        model = ApplicationModel
        fields = [
            "university_status",
            "faculty_status",
            "degree",
            "faculty",
            "field_of_study",

            "country",
            "agent",
            "gender",
            "min_age",
            "max_age",
            "more_than_one_request",
            "create_at"
        ]

    def get_more_than_one_request(self, queryset, name, value):
        users_with_count = UserModel.objects.annotate(application_count=Count("user_application"))
        users_with_multiple_applications = users_with_count.filter(application_count__gt=1)
        return queryset.filter(user__in=users_with_multiple_applications)

    def get_min_age(self, queryset, name, value):
        today = datetime.now().date()
        age = today.year - F('user__user_profile__birth_date__year') - (
                (today.month, today.day) < (
            F('user__user_profile__birth_date__month'), F('user__user_profile__birth_date__day')))
        return queryset.filter(user__user_profile__birth_date__lte=today,
                               user__user_profile__birth_date__gte=today.replace(year=today.year - int(value)))

    def get_max_age(self, queryset, name, value):
        today = datetime.now().date()
        age = today.year - F('user__user_profile__birth_date__year') - (
                (today.month, today.day) < (
            F('user__user_profile__birth_date__month'), F('user__user_profile__birth_date__day')))
        return queryset.filter(user__user_profile__birth_date__lte=today.replace(year=today.year - int(value) - 1))
