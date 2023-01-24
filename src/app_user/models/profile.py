from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from utils.general_models import GeneralDateModel

User = get_user_model()


class ProfileManager(models.Manager):
    pass


class Profile(GeneralDateModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User')
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name=_('First Name')
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name=_('Last Name')
    )
    birth_date = models.DateField(
        verbose_name=_('Birth Date'),
    )
    gender_options = [
        ('MAL', _('Male')),
        ('FML', _('FeMale')),
        ('OTR', _('Other'))
    ]
    gender = models.CharField(
        max_length=3,
        choices=gender_options,
        verbose_name=_('Gender')
    )
    nationality = models.CharField(
        max_length=50,
        verbose_name=_('Nationality')
    )
    mother_language = models.CharField(
        max_length=50,
        verbose_name=_('Mother Language')
    )
    other_languages = models.CharField(
        max_length=150,
        verbose_name=_('Other Languages'),
        null=True
    )
    language_status_options = [
        ('WEK', _('Weak')),
        ('GOD', _('Good')),
        ('EXT', _('Excellent'))
    ]
    english_status = models.CharField(
        max_length=3,
        choices=language_status_options,
        verbose_name=_('English Status')
    )
    persian_status = models.CharField(
        max_length=3,
        choices=language_status_options,
        verbose_name=_('Persian Status')
    )

    objects = ProfileManager()

    def __str__(self):
        return self.user.email
