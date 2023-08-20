from django.urls import path

from .views import *

app_name = 'app_application'
urlpatterns = [
    path('list/', ListAllApplicationsView.as_view(), name='application_all_list'),
    path('create/', ApplicationCreateView.as_view(), name='application_create'),
    path('detail_update/<int:pk>/', ApplicationDetailUpdateView.as_view(), name='application_detail_update'),

    path('document/create/', DocumentsCreateView.as_view(), name='application_create_document'),
    path('document/detail_update/<int:pk>/', DocumentsDetailUpdateView.as_view(), name='application_detail_update_document'),

    # admin
    path('admin/all-application/list/', AdminAllApplicationView.as_view(), name='admin_all_application_list'),
    path('admin/all-application/detail/<int:pk>/', AdminDetailApplicationView.as_view(), name='admin_application_detail'),
    path('admin/application/timeline/', AdminCreateApplicationTimeLineView.as_view(), name='admin_application_timeline_create'),
]
