from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

from app_user.models import ProfileModel, AddressModel
from app_education.models import (
    HighSchoolModel,
    BachelorDegreeModel,
    MasterDegreeModel,
)
from app_occupation.models import LatestOccupationModel

from utils import ManageMailService, RedisKeys

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_user_handler(sender, instance, **kwargs):
    if kwargs["created"]:
        if instance.is_agent:
            instance.locked = True
            instance.save()
        Token.objects.create(user=instance)
        ProfileModel.objects.create(user=instance)
        AddressModel.objects.create(user=instance)
        HighSchoolModel.objects.create(user=instance)
        BachelorDegreeModel.objects.create(user=instance)
        MasterDegreeModel.objects.create(user=instance)
        LatestOccupationModel.objects.create(user=instance)
        if instance.is_active is False:
            manage_email_obj = ManageMailService(instance.email)
            manage_email_obj.send_otp_code(RedisKeys.activate_account)
