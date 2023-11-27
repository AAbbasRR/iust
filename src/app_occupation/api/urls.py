from django.urls import path

from .views import *

app_name = "app_occupation"
urlpatterns = [
    path(
        "detail_update/",
        LatestOccupationDetailUpdateView.as_view(),
        name="occupation_detail_update",
    ),
]
