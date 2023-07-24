from django.db import models
from django.utils.translation import gettext as _

from app_user.models import UserModel

from utils.general_models import GeneralDateModel
from utils.data_list import gender_options, language_status_options


class ProfileManager(models.Manager):
    pass


class Profile(GeneralDateModel):
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ['-id']

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='user_profile',
        verbose_name=_('User')
    )
    phone_number = models.CharField(
        max_length=50,
        null=True,
        verbose_name=_('Phone Number')
    )
    first_name = models.CharField(
        max_length=100,
        null=True,
        verbose_name=_('First Name')
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
        verbose_name=_('Last Name')
    )
    birth_date = models.DateField(
        null=True,
        verbose_name=_('Birth Date'),
    )
    gender = models.CharField(
        max_length=3,
        null=True,
        choices=gender_options,
        default=gender_options[0][0],
        verbose_name=_('Gender')
    )
    nationality = models.CharField(
        max_length=50,
        null=True,
        verbose_name=_('Nationality')
    )
    mother_language = models.CharField(
        max_length=50,
        null=True,
        verbose_name=_('Mother Language')
    )
    other_languages = models.CharField(
        max_length=150,
        null=True,
        verbose_name=_('Other Languages'),
    )
    english_status = models.CharField(
        max_length=3,
        null=True,
        choices=language_status_options,
        default=language_status_options[1][0],
        verbose_name=_('English Status')
    )
    persian_status = models.CharField(
        max_length=3,
        null=True,
        choices=language_status_options,
        default=language_status_options[1][0],
        verbose_name=_('Persian Status')
    )

    objects = ProfileManager()

    def __str__(self):
        return self.user.email
