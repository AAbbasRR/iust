# Generated by Django 4.2.2 on 2023-07-20 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_application', '0015_alter_application_tracking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='tracking_id',
            field=models.CharField(default='de94db7b7e14', max_length=12, unique=True, verbose_name='Tracking ID'),
        ),
    ]