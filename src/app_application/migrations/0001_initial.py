# Generated by Django 4.1.5 on 2023-02-22 09:21

import app_application.models.documents
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('tracking_id', models.CharField(default='a841a7ad337d', max_length=12, unique=True, verbose_name='Tracking ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Full Name')),
                ('comments', models.TextField(verbose_name='Comments')),
                ('applied_program', models.BooleanField(default=False, verbose_name='Applied Program')),
                ('financial_self_support', models.BooleanField(default=True, verbose_name='Financial Self Support')),
                ('status', models.CharField(choices=[('CRNT', 'Current'), ('ACPT', 'Accepted'), ('RJCT', 'Rejected'), ('NTET', 'NeedToEdit')], max_length=4, verbose_name='Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_application', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('curriculum_vitae', models.ImageField(upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Curriculum Vitae')),
                ('personal_photo', models.ImageField(upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Personal photo')),
                ('valid_passport', models.ImageField(upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Valid')),
                ('high_school_certificate', models.ImageField(null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='High School Certificate')),
                ('trans_script_high_school_certificate', models.ImageField(null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Trans Script High School Certificate')),
                ('bachelor_degree', models.ImageField(null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Bachelor Degree')),
                ('trans_script_bachelor_degree', models.ImageField(null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Trans Script Bachelor Degree')),
                ('master_degree', models.ImageField(null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Master Degree')),
                ('trans_script_master_degree', models.ImageField(null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Trans Script Master Degree')),
                ('supporting_letter', models.ImageField(null=True, upload_to=app_application.models.documents.document_image_directory_path, verbose_name='Supporting Letter')),
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='application_document', to='app_application.application', verbose_name='Application')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
