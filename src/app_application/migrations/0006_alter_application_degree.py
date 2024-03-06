# Generated by Django 4.1.5 on 2023-12-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "app_application",
            "0005_alter_application_degree_alter_application_status_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="degree",
            field=models.CharField(
                choices=[
                    ("Bachelor", "Bachelor"),
                    ("Master", "Master"),
                    ("P.H.D", "P.H.D"),
                ],
                default="Bachelor",
                max_length=8,
                verbose_name="Degree",
            ),
        ),
    ]
