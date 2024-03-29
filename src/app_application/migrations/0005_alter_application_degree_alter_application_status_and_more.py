# Generated by Django 4.1.5 on 2023-12-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_application", "0004_referral"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="degree",
            field=models.CharField(
                choices=[
                    ("Bachelor", "Bachelor"),
                    ("Master", "Master"),
                    ("PHD", "P.H.D"),
                ],
                default="Bachelor",
                max_length=8,
                verbose_name="Degree",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="status",
            field=models.CharField(
                choices=[
                    ("Not_Completed", "Not Completed"),
                    ("Current", "Current"),
                    ("Accepted", "Accepted"),
                    ("Rejected", "Rejected"),
                    ("Need_To_Edit", "Need To Edit"),
                ],
                default="Not_Completed",
                max_length=13,
                verbose_name="Status",
            ),
        ),
        migrations.AlterField(
            model_name="timeline",
            name="status",
            field=models.CharField(
                choices=[
                    ("Confirmation", "Confirmation"),
                    ("Rejection", "Rejection"),
                    ("Investigation", "Investigation"),
                ],
                default="Investigation",
                max_length=13,
                verbose_name="Status",
            ),
        ),
    ]
