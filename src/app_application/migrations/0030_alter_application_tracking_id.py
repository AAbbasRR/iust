# Generated by Django 4.2.1 on 2023-07-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_application', '0029_alter_application_tracking_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='tracking_id',
            field=models.CharField(default='63ba1d7f2202', max_length=12, unique=True, verbose_name='Tracking ID'),
        ),
    ]
