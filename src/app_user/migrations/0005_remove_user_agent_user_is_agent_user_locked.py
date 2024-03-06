# Generated by Django 4.1.5 on 2024-01-09 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_user", "0004_alter_profile_english_status_alter_profile_gender_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="agent",
        ),
        migrations.AddField(
            model_name="user",
            name="is_agent",
            field=models.BooleanField(default=False, verbose_name="Is Agent"),
        ),
        migrations.AddField(
            model_name="user",
            name="locked",
            field=models.BooleanField(default=False, verbose_name="Is Locked"),
        ),
    ]
