from django.urls import path

from .views import *

app_name = 'app_occupation'
urlpatterns = [
    path('create/', LatestOccupationCreateView.as_view(), name='occupation_create'),
    path('detail_update/<str:tracking_id>/', LatestOccupationDetailUpdateView.as_view(), name='occupation_detail_update'),
]
