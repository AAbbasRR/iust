from django.db import models
from django.utils.translation import gettext as _

from Abrat.settings import DEBUG
from app_user.models import UserModel

from utils.general_models import GeneralDateModel
from utils.data_list import gender_options, language_status_options


class ProfileManager(models.Manager):
    pass


def profile_image_directory_path(instance, filename):
    return 'profile_images/user_{0}/{1}'.format(instance.user.email, filename)


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
    profile = models.ImageField(
        upload_to=profile_image_directory_path,
        null=True,
        blank=True,
        verbose_name=_('Profile')
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

    def profile_url(self, request):
        try:
            if self.profile is None or self.profile == "":
                return None
            else:
                host = request.get_host()
                protocol = request.build_absolute_uri().split(host)[0]
                protocol = protocol if DEBUG else protocol.replace("http", "https") if protocol.split(":")[0] == "http" else protocol
                website_url = protocol + host
                return website_url + self.profile.url
        except ValueError:
            return None
