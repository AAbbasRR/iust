from django.db import models
from django.utils.translation import gettext as _

from app_application.models import ApplicationModel

from utils.general_models import GeneralDateModel
from utils.data_list import degree_options, faculty_options, field_of_study_options


class ProgramRequestedManager(models.Manager):
    pass


class ProgramRequested(GeneralDateModel):
    application = models.OneToOneField(
        ApplicationModel,
        on_delete=models.CASCADE,
        related_name='application_program_requested',
        verbose_name=_('application')
    )
    degree = models.CharField(
        max_length=8,
        choices=degree_options,
        verbose_name=_('Degree')
    )
    faculty = models.CharField(
        max_length=80,
        choices=faculty_options,
        verbose_name=_('Faculty')
    )
    field_of_study = models.CharField(
        max_length=150,
        choices=field_of_study_options,
        verbose_name=_('Field Of Study')
    )

    objects = ProgramRequestedManager()

    def __str__(self):
        return self.application.user.email
