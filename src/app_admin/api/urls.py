from django.urls import path

from .views import *

app_name = 'app_admin'
urlpatterns = [
    # login
    path('login/', AdminLoginView.as_view(), name='admin_login'),
    path('oauth/', AdminOauthLoginAPIView.as_view(), name='admin_oauth_login'),
    path('report/countries/', AdminCountryRequestsCountAPIView.as_view(), name='admin_countries_report'),
    path('report/applications/', AdminReportApplicationsAPIView.as_view(), name='admin_applications_report'),
    path('report/diffrent/', AdminReportDiffrentBarAPIView.as_view(), name='admin_diffrent_report'),
]
