# Generated by Django 4.1.5 on 2023-11-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Admin",
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
                    "role",
                    models.CharField(
                        choices=[
                            ("staff", "Staff"),
                            ("prof", "Prof"),
                            ("karshenas", "Karshenas"),
                        ],
                        default="staff",
                        max_length=9,
                        verbose_name="Role",
                    ),
                ),
            ],
        ),
    ]
