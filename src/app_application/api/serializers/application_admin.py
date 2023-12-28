from django.db.models import Q, Case, When, Value, CharField

from django.utils.translation import gettext as _

from rest_framework import serializers, exceptions

from import_export import resources, fields

from app_application.models import ApplicationModel, DocumentModel, TimeLineModel
from app_user.models import UserModel
from app_admin.models import AdminModel

from utils.base_errors import BaseErrors


class AdminApplicationListSerializer(serializers.ModelSerializer):
    degree = serializers.CharField(source="get_degree_display", read_only=True)
    faculty = serializers.CharField(source="get_faculty_display", read_only=True)
    field_of_study = serializers.CharField(
        source="get_field_of_study_display", read_only=True
    )
    status = serializers.CharField(source="get_status_display", read_only=True)

    user = serializers.SerializerMethodField("get_user")

    class Meta:
        model = ApplicationModel
        fields = (
            "id",
            "tracking_id",
            "degree",
            "faculty",
            "field_of_study",
            "status",
            "jalali_created_at",
            "user",
        )

    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "agent": obj.user.agent,
            "full_name": obj.user.user_profile.get_full_name(),
            "gender": obj.user.user_profile.get_gender_display(),
            "country": obj.user.user_address.country,
            "age": obj.user.user_profile.age,
            "applications_count": obj.user.user_application.count(),
        }


class AdminApplicationExportResource(resources.ModelResource):
    degree = fields.Field(column_name=_("degree"))
    faculty = fields.Field(column_name=_("faculty"))
    field_of_study = fields.Field(column_name=_("field_of_study"))
    status = fields.Field(column_name=_("status"))
    jalali_created_at = fields.Field(column_name=_("jalali_created_at"))
    user_id = fields.Field(column_name=_("user_id"))
    user_agent = fields.Field(column_name=_("user_agent"))
    user_full_name = fields.Field(column_name=_("user_full_name"))
    user_gender = fields.Field(column_name=_("user_gender"))
    user_country = fields.Field(column_name=_("user_country"))
    user_age = fields.Field(column_name=_("user_age"))
    user_applications_count = fields.Field(column_name=_("user_applications_count"))

    class Meta:
        model = ApplicationModel
        fields = (
            "id",
            "tracking_id",
            "degree",
            "faculty",
            "field_of_study",
            "status",
            "jalali_created_at",
            "user_id",
            "user_agent",
            "user_full_name",
            "user_gender",
            "user_country",
            "user_age",
            "user_applications_count",
        )

    def dehydrate_degree(self, obj):
        return obj.get_degree_display()

    def dehydrate_faculty(self, obj):
        return obj.get_faculty_display()

    def dehydrate_field_of_study(self, obj):
        return obj.get_field_of_study_display()

    def dehydrate_university_status(self, obj):
        return obj.get_university_status_display()

    def dehydrate_faculty_status(self, obj):
        return obj.get_faculty_status_display()

    def dehydrate_jalali_created_at(self, obj):
        return obj.jalali_created_at()

    def dehydrate_user_id(self, obj):
        return obj.user.id

    def dehydrate_user_agent(self, obj):
        return obj.user.agent

    def dehydrate_user_full_name(self, obj):
        return obj.user.user_profile.get_full_name()

    def dehydrate_user_gender(self, obj):
        return obj.user.user_profile.gender

    def dehydrate_user_country(self, obj):
        return obj.user.user_address.country

    def dehydrate_user_age(self, obj):
        return obj.user.user_profile.age

    def dehydrate_user_applications_count(self, obj):
        return obj.user.user_application.count()


class AdminDocumentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = (
            "id",
            "jalali_created_at",
            "curriculum_vitae",
            "personal_photo",
            "valid_passport",
            "high_school_certificate",
            "trans_script_high_school_certificate",
            "bachelor_degree",
            "trans_script_bachelor_degree",
            "master_degree",
            "trans_script_master_degree",
            "supporting_letter",
        )

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.request = self.context.get("request")
        if self.request:
            self.user = self.request.user

    def get_curriculum_vitae(self, obj):
        return obj.get_field_image_url("curriculum_vitae", self.request)

    def get_personal_photo(self, obj):
        return obj.get_field_image_url("personal_photo", self.request)

    def get_valid_passport(self, obj):
        return obj.get_field_image_url("valid_passport", self.request)

    def get_high_school_certificate(self, obj):
        return obj.get_field_image_url("high_school_certificate", self.request)

    def get_trans_script_high_school_certificate(self, obj):
        return obj.get_field_image_url(
            "trans_script_high_school_certificate", self.request
        )

    def get_bachelor_degree(self, obj):
        return obj.get_field_image_url("bachelor_degree", self.request)

    def get_trans_script_bachelor_degree(self, obj):
        return obj.get_field_image_url("trans_script_bachelor_degree", self.request)

    def get_master_degree(self, obj):
        return obj.get_field_image_url("master_degree", self.request)

    def get_trans_script_master_degree(self, obj):
        return obj.get_field_image_url("trans_script_master_degree", self.request)

    def get_supporting_letter(self, obj):
        return obj.get_field_image_url("supporting_letter", self.request)


class AdminApplicationTimeLineSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_display", read_only=True)
    author = serializers.SerializerMethodField("get_author")

    class Meta:
        model = TimeLineModel
        fields = ("id", "status", "message", "jalali_created_at", "author")

    def get_author(self, obj):
        return {"full_name": obj.user.user_profile.get_full_name()}


class AdminRuleSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField("get_id")
    role_display = serializers.CharField(source="get_role_display", read_only=True)
    sub = serializers.SerializerMethodField("get_sub")
    username = serializers.SerializerMethodField("get_username")
    full_name = serializers.SerializerMethodField("get_full_name")

    class Meta:
        model = AdminModel
        fields = (
            "id",
            "role",
            "role_display",
            "sub",
            "username",
            "full_name",
        )

    def get_id(self, obj):
        return obj.user.id

    def get_sub(self, obj):
        return obj.user.sub

    def get_username(self, obj):
        return obj.user.username

    def get_full_name(self, obj):
        return obj.user.get_full_name()


class AdminDetailApplicationSerializer(serializers.ModelSerializer):
    degree = serializers.CharField(source="get_degree_display", read_only=True)
    faculty = serializers.CharField(source="get_faculty_display", read_only=True)
    field_of_study = serializers.CharField(
        source="get_field_of_study_display", read_only=True
    )
    status = serializers.CharField(source="get_status_display", read_only=True)
    user = serializers.SerializerMethodField("get_user")
    application_document = serializers.SerializerMethodField("get_application_document")
    application_timeline = serializers.SerializerMethodField("get_application_timeline")
    staffs = serializers.SerializerMethodField("get_staffs")
    can_referral = serializers.SerializerMethodField("get_can_referral")
    can_submit_application = serializers.SerializerMethodField(
        "get_can_submit_application"
    )

    class Meta:
        model = ApplicationModel
        fields = (
            "id",
            "tracking_id",
            "degree",
            "faculty",
            "field_of_study",
            "status",
            "jalali_created_at",
            "application_document",
            "application_timeline",
            "user",
            "staffs",
            "can_referral",
            "can_submit_application",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = self.context.get("request")
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ["PUT", "PATCH"]:
                for field_name, field in self.fields.items():
                    field.required = False

    def get_user(self, obj):
        return {
            "full_name": obj.user.user_profile.get_full_name(),
            "gender": obj.user.user_profile.gender,
            "country": obj.user.user_address.country,
            "city": obj.user.user_address.city,
            "age": obj.user.user_profile.age,
            "agent": obj.user.agent,
            "applications_count": obj.user.user_application.count(),
        }

    def get_application_document(self, obj):
        try:
            return AdminDocumentApplicationSerializer(
                obj.application_document,
                many=False,
                read_only=True,
                context=self.context,
            ).data
        except:
            return None

    def get_application_timeline(self, obj):
        return AdminApplicationTimeLineSerializer(
            obj.application_timeline.all(),
            many=True,
            read_only=True,
            context=self.context,
        ).data

    def get_can_referral(self, obj):
        user_rule = self.user.user_admin.filter(
            Q(schools=obj.faculty)
            & Q(role=AdminModel.AdminRoleOptions.faculty_director)
            | (
                Q(fields=obj.field_of_study)
                & Q(role=AdminModel.AdminRoleOptions.department_head)
            )
        ).first()
        return self.user.is_superuser or user_rule is not None

    def get_can_submit_application(self, obj):
        user_rule = self.user.user_admin.filter(
            schools=obj.faculty, role=AdminModel.AdminRoleOptions.faculty_director
        ).first()
        return self.user.is_superuser or user_rule is not None

    def get_staffs(self, obj):
        superusers_data = []
        superusers = UserModel.objects.filter(is_superuser=True).exclude(
            pk=self.user.id
        )
        for user in superusers:
            superusers_data.append(
                {
                    "id": user.id,
                    "role": "superuser",
                    "role_display": _("Superuser"),
                    "sub": user.sub,
                    "username": user.username,
                    "full_name": user.get_full_name(),
                }
            )
        staffs = (
            AdminModel.objects.filter(
                Q(schools=obj.faculty)
                & Q(role=AdminModel.AdminRoleOptions.faculty_director)
                | Q(fields=obj.field_of_study)
            )
            .exclude(pk=self.user.id)
            .annotate(
                custom_order=Case(
                    *[
                        When(role=value, then=Value(index))
                        for index, value in enumerate(
                            [
                                AdminModel.AdminRoleOptions.faculty_director,
                                AdminModel.AdminRoleOptions.department_head,
                                AdminModel.AdminRoleOptions.department_member,
                            ]
                        )
                    ],
                    default=Value(
                        len(
                            [
                                AdminModel.AdminRoleOptions.faculty_director,
                                AdminModel.AdminRoleOptions.department_head,
                                AdminModel.AdminRoleOptions.department_member,
                            ]
                        )
                    ),
                    output_field=CharField()
                )
            )
            .order_by("custom_order")
        )
        merged_users_data = AdminRuleSerializer(staffs, many=True).data
        return superusers_data + merged_users_data


class AdminUpdateApplicationSerializer(serializers.ModelSerializer):
    message = serializers.CharField(max_length=500, required=False, write_only=True)

    class Meta:
        model = ApplicationModel
        fields = ("status", "message")
        extra_kwargs = {"status": {"required": True}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = self.context.get("request")
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ["PUT", "PATCH"]:
                for field_name, field in self.fields.items():
                    field.required = False

    def update(self, instance, validated_data):
        user_rule = self.user.user_admin.filter(
            schools=instance.faculty, role=AdminModel.AdminRoleOptions.faculty_director
        ).first()
        if self.user.is_superuser or user_rule is not None:
            instance.status = validated_data["status"]
            instance.save()
            TimeLineModel.objects.create(
                user=self.user,
                application=instance,
                status=TimeLineModel.TimeLineStatusOptions.Confirmation
                if validated_data["status"]
                == ApplicationModel.ApplicationStatusOptions.Accepted
                else TimeLineModel.TimeLineStatusOptions.Rejection,
                message=validated_data.pop("message", "ثبت نهایی وضعیت پرونده"),
            )
            return instance
        else:
            raise exceptions.ParseError(BaseErrors.user_cant_edit_application_status)
