# Generated by Django 4.2.2 on 2023-07-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0010_user_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.TextField(null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=20, null=True, verbose_name='Postal Code'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='english_status',
            field=models.CharField(choices=[('WEK', 'Weak'), ('GOD', 'Good'), ('EXT', 'Excellent')], default='GOD', max_length=3, null=True, verbose_name='English Status'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=100, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('MAL', 'Male'), ('FML', 'FeMale'), ('OTR', 'Other')], max_length=3, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mother_language',
            field=models.CharField(max_length=50, null=True, verbose_name='Mother Language'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nationality',
            field=models.CharField(max_length=50, null=True, verbose_name='Nationality'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='persian_status',
            field=models.CharField(choices=[('WEK', 'Weak'), ('GOD', 'Good'), ('EXT', 'Excellent')], default='GOD', max_length=3, null=True, verbose_name='Persian Status'),
        ),
    ]
