# Generated by Django 4.1.5 on 2023-12-06 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_user", "0002_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, max_length=256, null=True, unique=True, verbose_name="Email"
            ),
        ),
    ]
