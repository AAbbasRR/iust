# Generated by Django 4.2.2 on 2023-07-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0011_alter_address_address_alter_address_postal_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=50, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('MAL', 'Male'), ('FML', 'FeMale'), ('OTR', 'Other')], default='MAL', max_length=3, null=True, verbose_name='Gender'),
        ),
    ]
