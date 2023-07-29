# Generated by Django 4.2.1 on 2023-07-29 13:02

import app_application.models.documents
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_application', '0025_alter_application_tracking_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_documents', to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='tracking_id',
            field=models.CharField(default='3afcebeeb4c1', max_length=12, unique=True, verbose_name='Tracking ID'),
        ),
        migrations.AlterField(
            model_name='document',
            name='application',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application_document', to='app_application.application', verbose_name='Application'),
        ),
        migrations.AlterField(
            model_name='document',
            name='bachelor_degree',
            field=models.ImageField(blank=True, null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Bachelor Degree'),
        ),
        migrations.AlterField(
            model_name='document',
            name='curriculum_vitae',
            field=models.ImageField(blank=True, null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Curriculum Vitae'),
        ),
        migrations.AlterField(
            model_name='document',
            name='high_school_certificate',
            field=models.ImageField(blank=True, null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='High School Certificate'),
        ),
        migrations.AlterField(
            model_name='document',
            name='master_degree',
            field=models.ImageField(blank=True, null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Master Degree'),
        ),
        migrations.AlterField(
            model_name='document',
            name='personal_photo',
            field=models.ImageField(blank=True, null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Personal photo'),
        ),
        migrations.AlterField(
            model_name='document',
            name='supporting_letter',
            field=models.ImageField(blank=True, null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Supporting Letter'),
        ),
        migrations.AlterField(
            model_name='document',
            name='trans_script_bachelor_degree',
            field=models.ImageField(blank=True, null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Trans Script Bachelor Degree'),
        ),
        migrations.AlterField(
            model_name='document',
            name='trans_script_high_school_certificate',
            field=models.ImageField(blank=True, null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Trans Script High School Certificate'),
        ),
        migrations.AlterField(
            model_name='document',
            name='trans_script_master_degree',
            field=models.ImageField(blank=True, null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Trans Script Master Degree'),
        ),
        migrations.AlterField(
            model_name='document',
            name='valid_passport',
            field=models.ImageField(blank=True, null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Valid'),
        ),
    ]
