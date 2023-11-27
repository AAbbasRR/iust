# Generated by Django 4.1.5 on 2023-11-27 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app_chat", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_messages",
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
        migrations.AddField(
            model_name="chatroom",
            name="members",
            field=models.ManyToManyField(
                related_name="user_chat_rooms",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Members",
            ),
        ),
    ]
