from django.http import HttpResponse
from django.db.models import Q

from rest_framework import generics

from app_application.models import ApplicationModel
from app_application.api.serializers.application_admin import (
    AdminApplicationListSerializer,
    AdminApplicationExportResource,
    AdminDetailApplicationSerializer,
    AdminUpdateApplicationSerializer,
)
from app_application.filters.applications import ApplicationListFilter
from app_admin.models import AdminModel

from utils.permissions import IsAuthenticatedPermission, IsAdminUserPermission
from utils.versioning import BaseVersioning
from utils.paginations import BasePagination


class AdminAllApplicationView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = AdminApplicationListSerializer
    ordering_fields = ["create_at"]
    filterset_class = ApplicationListFilter

    def get_queryset(self):
        if self.request.user.is_superuser is True:
            return ApplicationModel.objects.all().exclude(
                status=ApplicationModel.ApplicationStatusOptions.Not_Completed
            )
        else:
            user_faculty = (
                AdminModel.objects.filter(
                    user=self.request.user,
                    role=AdminModel.AdminRoleOptions.faculty_director,
                )
                .values_list("schools", flat=True)
                .distinct()
            )
            user_member_rules = AdminModel.objects.filter(
                user=self.request.user,
            )
            schools_list = list(
                user_member_rules.values_list("schools", flat=True).distinct()
            )
            fields_list = list(
                user_member_rules.values_list("fields", flat=True).distinct()
            )
            director_applications = ApplicationModel.objects.filter(
                faculty__in=list(user_faculty)
            ).exclude(status=ApplicationModel.ApplicationStatusOptions.Not_Completed)
            member_applications = ApplicationModel.objects.filter(
                Q(faculty__in=schools_list) & Q(field_of_study__in=fields_list)
            ).exclude(status=ApplicationModel.ApplicationStatusOptions.Not_Completed)
            merged_queryset = director_applications | member_applications
            return merged_queryset


class AdminExportApplicationListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning
    ordering_fields = ["create_at"]
    filterset_class = ApplicationListFilter

    def get_queryset(self):
        if self.request.user.is_superuser is True:
            return ApplicationModel.objects.all().exclude(
                status=ApplicationModel.ApplicationStatusOptions.Not_Completed
            )
        else:
            user_faculty = (
                AdminModel.objects.filter(
                    user=self.request.user,
                    role=AdminModel.AdminRoleOptions.faculty_director,
                )
                .values_list("schools", flat=True)
                .distinct()
            )
            user_member_rules = AdminModel.objects.filter(
                user=self.request.user,
            )
            schools_list = list(
                user_member_rules.values_list("schools", flat=True).distinct()
            )
            fields_list = list(
                user_member_rules.values_list("fields", flat=True).distinct()
            )
            director_applications = ApplicationModel.objects.filter(
                faculty__in=list(user_faculty)
            ).exclude(status=ApplicationModel.ApplicationStatusOptions.Not_Completed)
            member_applications = ApplicationModel.objects.filter(
                Q(faculty__in=schools_list) & Q(field_of_study__in=fields_list)
            ).exclude(status=ApplicationModel.ApplicationStatusOptions.Not_Completed)
            merged_queryset = director_applications | member_applications
            return merged_queryset

    def get(self, *args, **kwargs):
        resource_class = AdminApplicationExportResource()
        dataset = resource_class.export(self.get_queryset())

        response = HttpResponse(dataset.xlsx, content_type="text/xlsx")
        response["Content-Disposition"] = 'attachment; filename="export_orders.xlsx"'
        return response


class AdminReferralApplicationListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning
    pagination_class = BasePagination
    serializer_class = AdminApplicationListSerializer
    ordering_fields = ["create_at"]
    filterset_class = ApplicationListFilter

    def get_queryset(self):
        return ApplicationModel.objects.filter(
            application_referral__destination_user=self.request.user,
            application_referral__is_enabled=True,
        ).distinct()


class AdminExportReferralApplicationListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning
    ordering_fields = ["create_at"]
    filterset_class = ApplicationListFilter

    def get_queryset(self):
        return ApplicationModel.objects.filter(
            application_referral__destination_user=self.request.user,
            application_referral__is_enabled=True,
        ).distinct()

    def get(self, *args, **kwargs):
        resource_class = AdminApplicationExportResource()
        dataset = resource_class.export(self.get_queryset())

        response = HttpResponse(dataset.xlsx, content_type="text/xlsx")
        response["Content-Disposition"] = 'attachment; filename="export_orders.xlsx"'
        return response


class AdminDetailApplicationView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning
    serializer_class = AdminDetailApplicationSerializer
    lookup_field = "pk"

    def get_queryset(self):
        if self.request.user.is_superuser is True:
            return ApplicationModel.objects.all().exclude(
                status=ApplicationModel.ApplicationStatusOptions.Not_Completed
            )
        else:
            user_faculty = (
                AdminModel.objects.filter(
                    user=self.request.user,
                    role=AdminModel.AdminRoleOptions.faculty_director,
                )
                .values_list("schools", flat=True)
                .distinct()
            )
            user_member_rules = AdminModel.objects.filter(
                user=self.request.user,
            )
            schools_list = list(
                user_member_rules.values_list("schools", flat=True).distinct()
            )
            fields_list = list(
                user_member_rules.values_list("fields", flat=True).distinct()
            )
            director_applications = ApplicationModel.objects.filter(
                faculty__in=list(user_faculty)
            ).exclude(status=ApplicationModel.ApplicationStatusOptions.Not_Completed)
            member_applications = ApplicationModel.objects.filter(
                Q(faculty__in=schools_list) & Q(field_of_study__in=fields_list)
            ).exclude(status=ApplicationModel.ApplicationStatusOptions.Not_Completed)
            merged_queryset = director_applications | member_applications
            return merged_queryset


class AdminUpdateApplicationView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticatedPermission, IsAdminUserPermission]
    versioning_class = BaseVersioning
    serializer_class = AdminUpdateApplicationSerializer
    lookup_field = "pk"

    def get_queryset(self):
        if self.request.user.is_superuser is True:
            return ApplicationModel.objects.all().exclude(
                status=ApplicationModel.ApplicationStatusOptions.Not_Completed
            )
        else:
            user_faculty = (
                AdminModel.objects.filter(
                    user=self.request.user,
                    role=AdminModel.AdminRoleOptions.faculty_director,
                )
                .values_list("schools", flat=True)
                .distinct()
            )
            return ApplicationModel.objects.filter(
                faculty__in=list(user_faculty)
            ).exclude(status=ApplicationModel.ApplicationStatusOptions.Not_Completed)
