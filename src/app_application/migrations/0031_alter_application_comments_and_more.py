# Generated by Django 4.1.5 on 2023-07-29 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_application', '0030_alter_application_tracking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='comments',
            field=models.TextField(blank=True, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='application',
            name='full_name',
            field=models.CharField(max_length=50, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='application',
            name='tracking_id',
            field=models.CharField(default='a306589dd629', max_length=12, unique=True, verbose_name='Tracking ID'),
        ),
    ]
