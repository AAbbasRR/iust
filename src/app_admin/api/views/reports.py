from django.db.models import (
    Count,
)

from rest_framework import generics, response

from app_application.models import ApplicationModel
from app_user.models import AddressModel, ProfileModel

from utils.versioning import BaseVersioning
from utils.permissions import IsAuthenticatedPermission, IsAdminPermission

from jdatetime import (
    datetime,
    timedelta,
)


class AdminCountryRequestsCountAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminPermission]
    versioning_class = BaseVersioning

    def get(self, *args, **kwargs):
        tab_filter = self.request.query_params.get("date", "all")
        if tab_filter == "all":
            application_count = ApplicationModel.objects.all().count()
            applications_by_country = AddressModel.objects.exclude(country=None).values('country').annotate(
                total_applications=Count('user__user_application'))
            sorted_applications = sorted(applications_by_country, key=lambda x: x['total_applications'], reverse=True)
            return response.Response({
                "application_count": application_count,
                "countries": sorted_applications
            })
            # first_month = (
            #     datetime.now()
            #     .replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            #     .togregorian()
            # )
            # date_filter = date_filter - timedelta(days=365)


class AdminReportApplicationsAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminPermission]
    versioning_class = BaseVersioning

    def get(self, *args, **kwargs):
        tab_filter = self.request.query_params.get("date", "all")
        if tab_filter == "all":
            application_count = ApplicationModel.objects.exclude(status="NOCO").count()
            return response.Response({
                "application_count": application_count,
                "report": {
                    "crnt_count": ApplicationModel.objects.filter(status='CRNT').count(),
                    "acpt_count": ApplicationModel.objects.filter(status='ACPT').count(),
                    "rjct_count": ApplicationModel.objects.filter(status='RJCT').count(),
                    "ntet_count": ApplicationModel.objects.filter(status='NTET').count(),
                }
            })
            # first_month = (
            #     datetime.now()
            #     .replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            #     .togregorian()
            # )
            # date_filter = date_filter - timedelta(days=365)


class AdminReportDiffrentBarAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminPermission]
    versioning_class = BaseVersioning

    def get(self, *args, **kwargs):
        tab_filter = self.request.query_params.get("date", "all")
        if tab_filter == "all":
            application_count = ApplicationModel.objects.all().count()
            return response.Response({
                "application_count": application_count,
                "gender": {
                    "male": ApplicationModel.objects.filter(user__user_profile__gender="MAL").count(),
                    "female": ApplicationModel.objects.filter(user__user_profile__gender="FML").count(),
                },
                "education": {
                    "bachelor": ApplicationModel.objects.filter(degree="Bachelor").count(),
                    "master": ApplicationModel.objects.filter(degree="Master").count(),
                    "phd": ApplicationModel.objects.filter(degree="P.H.D").count(),
                }
            })
            # first_month = (
            #     datetime.now()
            #     .replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            #     .togregorian()
            # )
            # date_filter = date_filter - timedelta(days=365)
