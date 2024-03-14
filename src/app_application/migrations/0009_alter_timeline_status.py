# Generated by Django 4.1.5 on 2024-01-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_application", "0008_application_agent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timeline",
            name="status",
            field=models.CharField(
                choices=[
                    ("Confirmation", "Confirmation"),
                    ("Rejection", "Rejection"),
                    ("Investigation", "Investigation"),
                    ("Referral", "Referral"),
                    ("NeedToEdit", "Need To Edit"),
                ],
                default="Investigation",
                max_length=13,
                verbose_name="Status",
            ),
        ),
    ]