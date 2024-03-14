from django.db.models import Count
from django.utils import timezone

from rest_framework import generics, response

from app_application.models import ApplicationModel
from app_user.models import AddressModel, ProfileModel

from utils.versioning import BaseVersioning
from utils.permissions import IsAuthenticatedPermission, IsAdminUserPermission

from datetime import timedelta


class AdminCountryRequestsCountAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning

    def get(self, *args, **kwargs):
        tab_filter = self.request.query_params.get("date", "all")
        if tab_filter == "all":
            application_count = ApplicationModel.objects.all().count()
            applications_by_country = (
                AddressModel.objects.exclude(country=None)
                .values("country")
                .annotate(total_applications=Count("user__user_application"))
            )
            sorted_applications = sorted(
                applications_by_country,
                key=lambda x: x["total_applications"],
                reverse=True,
            )
            return response.Response(
                {
                    "application_count": application_count,
                    "countries": sorted_applications,
                }
            )
            # first_month = (
            #     datetime.now()
            #     .replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            #     .togregorian()
            # )
            # date_filter = date_filter - timedelta(days=365)


class AdminReportApplicationsAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning

    def get(self, *args, **kwargs):
        tab_filter = self.request.query_params.get("date", "all")
        if tab_filter == "all":
            application_count = ApplicationModel.objects.exclude(
                status=ApplicationModel.ApplicationStatusOptions.Not_Completed
            ).count()
            return response.Response(
                {
                    "application_count": application_count,
                    "report": {
                        "crnt_count": ApplicationModel.objects.filter(
                            status=ApplicationModel.ApplicationStatusOptions.Current
                        ).count(),
                        "acpt_count": ApplicationModel.objects.filter(
                            status=ApplicationModel.ApplicationStatusOptions.Accepted
                        ).count(),
                        "rjct_count": ApplicationModel.objects.filter(
                            status=ApplicationModel.ApplicationStatusOptions.Rejected
                        ).count(),
                        "ntet_count": ApplicationModel.objects.filter(
                            status=ApplicationModel.ApplicationStatusOptions.NeedToEdit
                        ).count(),
                    },
                }
            )
            # first_month = (
            #     datetime.now()
            #     .replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            #     .togregorian()
            # )
            # date_filter = date_filter - timedelta(days=365)


class AdminReportDiffrentBarAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning

    def get(self, *args, **kwargs):
        tab_filter = self.request.query_params.get("date", "all")
        if tab_filter == "all":
            application_count = ApplicationModel.objects.all().count()
            return response.Response(
                {
                    "application_count": application_count,
                    "gender": {
                        "male": ApplicationModel.objects.filter(
                            user__user_profile__gender=ProfileModel.ProfileGenderOptions.Male
                        ).count(),
                        "female": ApplicationModel.objects.filter(
                            user__user_profile__gender=ProfileModel.ProfileGenderOptions.FeMale
                        ).count(),
                    },
                    "education": {
                        "bachelor": ApplicationModel.objects.filter(
                            degree=ApplicationModel.ApplicationDegreeOptions.Bachelor
                        ).count(),
                        "master": ApplicationModel.objects.filter(
                            degree=ApplicationModel.ApplicationDegreeOptions.Master
                        ).count(),
                        "phd": ApplicationModel.objects.filter(
                            degree=ApplicationModel.ApplicationDegreeOptions.PHD
                        ).count(),
                    },
                }
            )
            # first_month = (
            #     datetime.now()
            #     .replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            #     .togregorian()
            # )
            # date_filter = date_filter - timedelta(days=365)


class AdminReportHitMapAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission]
    versioning_class = BaseVersioning

    def get(self, *args, **kwargs):
        tab_filter = self.request.query_params.get("date", "month")
        if tab_filter == "month":
            thirty_days_ago = timezone.now() - timedelta(days=30)
            applications_last_30_days = (
                ApplicationModel.objects.filter(create_at__gte=thirty_days_ago)
                .annotate(date=timezone.trunc("day", "create_at"))
                .values("date")
                .annotate(count=Count("id"))
                .order_by("-date")
            )
            data_dict = {}
            for application in applications_last_30_days:
                date = application["date"].strftime("%Y-%m-%d")
                count = application["count"]
                data_dict[date] = count
            date_range = [thirty_days_ago + timedelta(days=x) for x in range(30)]
            for date in date_range:
                date_str = date.strftime("%Y-%m-%d")
                if date_str not in data_dict:
                    data_dict[date_str] = 0
            return response.Response(
                [{"value": count, "day": day} for day, count in data_dict.items()]
            )
