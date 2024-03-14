# Generated by Django 4.1.5 on 2023-12-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_notification", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="status",
            field=models.CharField(
                choices=[
                    ("Information", "Information"),
                    ("Success", "Success"),
                    ("Warning", "Warning"),
                    ("Error", "Error"),
                ],
                default="Information",
                max_length=11,
                verbose_name="Status",
            ),
        ),
    ]