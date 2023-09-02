# Generated by Django 4.2.1 on 2023-07-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_occupation', '0005_alter_latestoccupation_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestoccupation',
            name='city',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='latestoccupation',
            name='country',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Country'),
        ),
    ]
