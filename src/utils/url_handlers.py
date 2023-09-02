from django.http import HttpResponseServerError, HttpResponseNotFound, JsonResponse

from .base_errors import BaseErrors


def custom_404_response(request, exception):
    return HttpResponseNotFound(JsonResponse({
        "status": False,
        "message": BaseErrors.url_not_found
    }))


def custom_500_response(request):
    return HttpResponseServerError(JsonResponse({
        "status": False,
        "message": BaseErrors.server_error
    }))
