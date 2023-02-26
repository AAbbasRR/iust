from django.db import models
from django.utils.translation import gettext as _

from app_application.models import ApplicationModel

from utils import GeneralDateModel


class DocumentManager(models.Manager):
    pass


def document_image_directory_path(instance, filename):
    return 'application_documents/user_{0}/{1}/{2}'.format(instance.application.user.email, instance.application.tracking_id, filename)


class Document(GeneralDateModel):
    application = models.OneToOneField(
        ApplicationModel,
        on_delete=models.CASCADE,
        related_name='application_document',
        verbose_name=_('Application')
    )
    curriculum_vitae = models.ImageField(
        upload_to=document_image_directory_path,
        verbose_name=_('Curriculum Vitae')
    )
    personal_photo = models.ImageField(
        upload_to=document_image_directory_path,
        verbose_name=_('Personal photo')
    )
    valid_passport = models.ImageField(
        upload_to=document_image_directory_path,
        verbose_name=_('Valid')
    )
    high_school_certificate = models.ImageField(
        upload_to=document_image_directory_path,
        null=True,
        verbose_name=_('High School Certificate')
    )
    trans_script_high_school_certificate = models.ImageField(
        upload_to=document_image_directory_path,
        null=True,
        verbose_name=_('Trans Script High School Certificate')
    )
    bachelor_degree = models.ImageField(
        upload_to=document_image_directory_path,
        null=True,
        verbose_name=_('Bachelor Degree')
    )
    trans_script_bachelor_degree = models.ImageField(
        upload_to=document_image_directory_path,
        null=True,
        verbose_name=_('Trans Script Bachelor Degree')
    )
    master_degree = models.ImageField(
        upload_to=document_image_directory_path,
        null=True,
        verbose_name=_('Master Degree')
    )
    trans_script_master_degree = models.ImageField(
        upload_to=document_image_directory_path,
        null=True,
        verbose_name=_('Trans Script Master Degree')
    )
    supporting_letter = models.ImageField(
        upload_to=document_image_directory_path,
        null=True,
        verbose_name=_('Supporting Letter')
    )