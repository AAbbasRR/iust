# Generated by Django 4.2.1 on 2023-07-29 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_occupation', '0003_alter_latestoccupation_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latestoccupation',
            name='application',
        ),
        migrations.AddField(
            model_name='latestoccupation',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_latest_occupation', to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
    ]