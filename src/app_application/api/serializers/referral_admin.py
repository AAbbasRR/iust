from rest_framework import serializers, exceptions

from app_admin.models import AdminModel
from app_application.models import ReferralModel, TimeLineModel

from utils.base_errors import BaseErrors


class AdminCreateReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralModel
        fields = ("application", "destination_user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = self.context.get("request")
        if self.request:
            self.user = self.request.user
            self.method = self.request.method
            if self.method in ["PUT", "PATCH"]:
                for field_name, field in self.fields.items():
                    field.required = False

    def validate(self, attrs):
        if self.user.is_superuser is True:
            user_faculty_rule = (
                attrs["destination_user"]
                .user_admin.filter(
                    role=AdminModel.AdminRoleOptions.faculty_director,
                    schools=attrs["application"].faculty,
                )
                .first()
            )
            if (
                attrs["destination_user"].is_superuser is True
                or user_faculty_rule is not None
            ):
                ReferralModel.objects.create(origin_user=self.user, **attrs)
                role = (
                    "مدیر اصلی"
                    if attrs["destination_user"].is_superuser
                    else "مدیر دانشکده"
                )
                TimeLineModel.objects.create(
                    application=attrs["application"],
                    user=self.user,
                    status=TimeLineModel.TimeLineStatusOptions.Investigation,
                    message=f"ارجاع به {role} ({attrs['destination_user'].get_full_name()}) با کد پرسنلی {attrs['destination_user'].sub}",
                )
            else:
                user_head_rule = (
                    attrs["destination_user"]
                    .user_admin.filter(
                        role=AdminModel.AdminRoleOptions.department_head,
                        schools=attrs["application"].faculty,
                        fields=attrs["application"].field_of_study,
                    )
                    .first()
                )
                if user_head_rule is not None:
                    application_members_rule = AdminModel.objects.filter(
                        role=AdminModel.AdminRoleOptions.department_member,
                        schools=attrs["application"].faculty,
                        fields=attrs["application"].field_of_study,
                    )
                    ReferralModel.objects.create(origin_user=self.user, **attrs)
                    for member in application_members_rule:
                        ReferralModel.objects.create(
                            origin_user=self.user,
                            destination_user=member.user,
                            application=attrs["application"],
                        )
                    TimeLineModel.objects.create(
                        application=attrs["application"],
                        user=self.user,
                        status=TimeLineModel.TimeLineStatusOptions.Investigation,
                        message=f"ارجاع به مدیر گروه ({attrs['destination_user'].get_full_name()}) با کد پرسنلی {attrs['destination_user'].sub} و تمام اعضای گروه ",
                    )
                else:
                    raise exceptions.ParseError(BaseErrors.cant_referral_to_this_user)
        else:
            user_faculty_rule = self.user.user_admin.filter(
                role=AdminModel.AdminRoleOptions.faculty_director,
                schools=attrs["application"].faculty,
            ).first()
            if user_faculty_rule is not None:
                if attrs["destination_user"].is_superuser is True:
                    ReferralModel.objects.create(origin_user=self.user, **attrs)
                    TimeLineModel.objects.create(
                        application=attrs["application"],
                        user=self.user,
                        status=TimeLineModel.TimeLineStatusOptions.Investigation,
                        message=f"ارجاع به مدیر اصلی ({attrs['destination_user'].get_full_name()}) با کد پرسنلی {attrs['destination_user'].sub}",
                    )
                else:
                    user_member_head_rule = (
                        attrs["destination_user"]
                        .user_admin.filter(
                            role=AdminModel.AdminRoleOptions.department_head,
                            schools=attrs["application"].faculty,
                            fields=attrs["application"].field_of_study,
                        )
                        .first()
                    )
                    if user_member_head_rule is not None:
                        application_members_rule = AdminModel.objects.filter(
                            role=AdminModel.AdminRoleOptions.department_member,
                            schools=attrs["application"].faculty,
                            fields=attrs["application"].field_of_study,
                        )
                        ReferralModel.objects.create(origin_user=self.user, **attrs)
                        for member in application_members_rule:
                            ReferralModel.objects.create(
                                origin_user=self.user,
                                destination_user=member.user,
                                application=attrs["application"],
                            )
                        TimeLineModel.objects.create(
                            application=attrs["application"],
                            user=self.user,
                            status=TimeLineModel.TimeLineStatusOptions.Investigation,
                            message=f"ارجاع به مدیر گروه ({attrs['destination_user'].get_full_name()}) با کد پرسنلی {attrs['destination_user'].sub} و تمام اعضای گروه ",
                        )
                    else:
                        raise exceptions.ParseError(
                            BaseErrors.cant_referral_to_this_user
                        )
            else:
                user_head_rule = self.user.user_admin.filter(
                    role=AdminModel.AdminRoleOptions.department_head,
                    schools=attrs["application"].faculty,
                    fields=attrs["application"].field_of_study,
                ).first()
                if user_head_rule is not None:
                    user_faculty_rule = (
                        attrs["destination_user"]
                        .user_admin.filter(
                            role=AdminModel.AdminRoleOptions.faculty_director,
                            schools=attrs["application"].faculty,
                        )
                        .first()
                    )
                    if user_faculty_rule is not None:
                        ReferralModel.objects.create(origin_user=self.user, **attrs)
                        TimeLineModel.objects.create(
                            application=attrs["application"],
                            user=self.user,
                            status=TimeLineModel.TimeLineStatusOptions.Investigation,
                            message=f"ارجاع به مدیر دانشکده ({attrs['destination_user'].get_full_name()}) با کد پرسنلی {attrs['destination_user'].sub}",
                        )
                    else:
                        raise exceptions.ParseError(
                            BaseErrors.cant_referral_to_this_user
                        )
                else:
                    raise exceptions.ParseError(
                        BaseErrors.user_do_not_have_rule_for_referral
                    )

        return True
