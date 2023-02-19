# Generated by Django 4.1.5 on 2023-02-13 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0003_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city_code',
            field=models.CharField(max_length=5, null=True, verbose_name='City Code'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country_code',
            field=models.CharField(max_length=5, null=True, verbose_name='Country Code'),
        ),
    ]
