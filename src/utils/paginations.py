from rest_framework import pagination
from rest_framework.response import Response


class BasePagination(pagination.PageNumberPagination):
    page_size = 15
    page_size_query_param = "page_size"

    def __init__(self):
        self.count = None

    def paginate_queryset(self, queryset, request, view=None):
        self.count = queryset.count()
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response(
            {
                "total": self.page.paginator.num_pages,
                "count_all": self.count,
                "results": data,
            }
        )
