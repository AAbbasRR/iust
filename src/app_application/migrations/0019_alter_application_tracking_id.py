# Generated by Django 4.2.2 on 2023-07-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_application', '0018_alter_application_tracking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='tracking_id',
            field=models.CharField(default='958a4009da08', max_length=12, unique=True, verbose_name='Tracking ID'),
        ),
    ]