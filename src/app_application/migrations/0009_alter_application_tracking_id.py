# Generated by Django 4.1.5 on 2023-02-28 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_application', '0008_alter_application_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='tracking_id',
            field=models.CharField(default='0b85f9dc8e76', max_length=12, unique=True, verbose_name='Tracking ID'),
        ),
    ]
