# Generated by Django 4.1.5 on 2023-11-27 12:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BachelorDegree",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created Time"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated Time"),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=35, null=True, verbose_name="Country"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=40, null=True, verbose_name="City"
                    ),
                ),
                (
                    "date_of_graduation",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date Of Graduation"
                    ),
                ),
                (
                    "gpa",
                    models.FloatField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="GPA",
                    ),
                ),
                (
                    "field_of_study",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Field Of Study",
                    ),
                ),
                (
                    "university",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="University"
                    ),
                ),
            ],
            options={
                "verbose_name": "Bachelor Degree",
                "verbose_name_plural": "Bachelor Degrees",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="HighSchool",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created Time"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated Time"),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=35, null=True, verbose_name="Country"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=40, null=True, verbose_name="City"
                    ),
                ),
                (
                    "date_of_graduation",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date Of Graduation"
                    ),
                ),
                (
                    "gpa",
                    models.FloatField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="GPA",
                    ),
                ),
                (
                    "field_of_study",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Field Of Study",
                    ),
                ),
            ],
            options={
                "verbose_name": "High School",
                "verbose_name_plural": "High Schools",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="MasterDegree",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created Time"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated Time"),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=35, null=True, verbose_name="Country"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=40, null=True, verbose_name="City"
                    ),
                ),
                (
                    "date_of_graduation",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date Of Graduation"
                    ),
                ),
                (
                    "gpa",
                    models.FloatField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="GPA",
                    ),
                ),
                (
                    "field_of_study",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Field Of Study",
                    ),
                ),
                (
                    "university",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="University"
                    ),
                ),
            ],
            options={
                "verbose_name": "MasterDegree",
                "verbose_name_plural": "Master Degrees",
                "ordering": ["-id"],
            },
        ),
    ]
