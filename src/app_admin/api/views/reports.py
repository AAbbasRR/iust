from django.db.models import Count
from django.utils import timezone

from rest_framework import generics, response

from app_application.models import ApplicationModel
from app_user.models import AddressModel, ProfileModel

from utils.versioning import BaseVersioning
from utils.permissions import IsAuthenticatedPermission, IsAdminUserPermission
from utils.data_list import countries

from datetime import timedelta


class AdminCountryRequestsCountAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning

    def get(self, *args, **kwargs):
        tab_filter = self.request.query_params.get("date", "all")
        if tab_filter == "all":
            application_count = ApplicationModel.objects.exclude(
                status=ApplicationModel.ApplicationStatusOptions.Not_Completed
            ).count()
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
            application_count = ApplicationModel.objects.exclude(
                status=ApplicationModel.ApplicationStatusOptions.Not_Completed
            ).count()
            return response.Response(
                {
                    "application_count": application_count,
                    "gender": {
                        "male": ApplicationModel.objects.filter(
                            user__user_profile__gender=ProfileModel.ProfileGenderOptions.Male
                        )
                        .exclude(
                            status=ApplicationModel.ApplicationStatusOptions.Not_Completed
                        )
                        .count(),
                        "female": ApplicationModel.objects.filter(
                            user__user_profile__gender=ProfileModel.ProfileGenderOptions.FeMale
                        )
                        .exclude(
                            status=ApplicationModel.ApplicationStatusOptions.Not_Completed
                        )
                        .count(),
                    },
                    "education": {
                        "bachelor": ApplicationModel.objects.filter(
                            degree=ApplicationModel.ApplicationDegreeOptions.Bachelor
                        )
                        .exclude(
                            status=ApplicationModel.ApplicationStatusOptions.Not_Completed
                        )
                        .count(),
                        "master": ApplicationModel.objects.filter(
                            degree=ApplicationModel.ApplicationDegreeOptions.Master
                        )
                        .exclude(
                            status=ApplicationModel.ApplicationStatusOptions.Not_Completed
                        )
                        .count(),
                        "phd": ApplicationModel.objects.filter(
                            degree=ApplicationModel.ApplicationDegreeOptions.PHD
                        )
                        .exclude(
                            status=ApplicationModel.ApplicationStatusOptions.Not_Completed
                        )
                        .count(),
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
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning

    def get(self, *args, **kwargs):
        tab_filter = self.request.query_params.get("date", "month")
        if tab_filter == "month":
            thirty_days_ago = timezone.now() - timedelta(days=30)
            applications_last_30_days = (
                ApplicationModel.objects.filter(create_at__gte=thirty_days_ago)
                .exclude(status=ApplicationModel.ApplicationStatusOptions.Not_Completed)
                .values("create_at__date")
                .annotate(count=Count("id"))
                .order_by("-create_at__date")
            )

            serialized_data = []
            for single_date in (thirty_days_ago + timedelta(n) for n in range(30)):
                day_str = single_date.strftime("%Y-%m-%d")
                count_dict = next(
                    (
                        item
                        for item in applications_last_30_days
                        if item["create_at__date"] == single_date
                    ),
                    None,
                )

                count = count_dict["count"] if count_dict else 0
                serialized_data.append({"value": count, "day": day_str})
            return response.Response(serialized_data)


class AdminReportCountryAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning

    def get(self, *args, **kwargs):
        tab_filter = self.request.query_params.get("date", "all")
        if tab_filter == "all":
            applications_by_country = list(
                ApplicationModel.objects.exclude(
                    status=ApplicationModel.ApplicationStatusOptions.Not_Completed
                )
                .select_related("user__user_address")
                .values("user__user_address__country")
                .annotate(application_count=Count("id"))
                .order_by("-application_count")
            )

            return response.Response(
                [
                    {
                        "id": countries[entry["user__user_address__country"]],
                        "value": entry["application_count"],
                    }
                    for entry in applications_by_country
                ]
            )


class AdminReportBarChartAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning

    def get(self, *args, **kwargs):
        tab_filter = self.request.query_params.get("date", "month")
        if tab_filter == "month":
            faculty_filter = self.request.query_params.get("faculty")
            thirty_days_ago = timezone.now() - timedelta(days=30)
            applications_last_30_days = (
                ApplicationModel.objects.filter(
                    create_at__gte=thirty_days_ago, faculty=faculty_filter
                )
                .exclude(status=ApplicationModel.ApplicationStatusOptions.Not_Completed)
                .values("create_at__date", "degree")
                .annotate(count=Count("id"))
            )

            counts_per_day_and_degree = {}
            for entry in applications_last_30_days:
                date_str = entry["create_at__date"].strftime("%Y-%m-%d")
                degree = entry["degree"]
                count = entry["count"]

                if date_str not in counts_per_day_and_degree:
                    counts_per_day_and_degree[date_str] = {
                        "phd": 0,
                        "bachelor": 0,
                        "master": 0,
                    }

                counts_per_day_and_degree[date_str][degree.lower()] = count

            return response.Response(counts_per_day_and_degree)
