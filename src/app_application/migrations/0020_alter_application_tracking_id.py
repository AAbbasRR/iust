# Generated by Django 4.2.2 on 2023-07-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_application', '0019_alter_application_tracking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='tracking_id',
            field=models.CharField(default='1972fb9cd064', max_length=12, unique=True, verbose_name='Tracking ID'),
        ),
    ]