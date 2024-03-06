from django.db.models import Count, F

from django_filters import (
    FilterSet,
    BooleanFilter,
)

from app_chat.models import ChatRoomModel


class AdminTicketListFilter(FilterSet):
    my_tickets = BooleanFilter(method="get_my_tickets")

    class Meta:
        model = ChatRoomModel
        fields = [
            "status",
            "my_tickets",
        ]

    def get_my_tickets(self, queryset, name, value):
        if value is True:
            return queryset.filter(members=self.request.user)
        else:
            return queryset.annotate(num_members=Count("members")).filter(num_members=1)
