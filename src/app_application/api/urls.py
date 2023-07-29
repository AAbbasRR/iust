from django.urls import path

from .views import *

app_name = 'app_application'
urlpatterns = [
    path('list/', ListAllApplicationsView.as_view(), name='application_all_list'),
    path('create/', ApplicationCreateView.as_view(), name='application_create'),
    path('detail_update/<str:tracking_id>/', ApplicationDetailUpdateView.as_view(), name='application_detail_update'),

    path('document/create/', DocumentsCreateView.as_view(), name='application_create_document'),
    path('document/detail_update/<int:pk>/', DocumentsDetailUpdateView.as_view(), name='application_detail_update_document'),
]
