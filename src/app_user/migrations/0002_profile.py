# Generated by Django 4.1.5 on 2023-01-24 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('gender', models.CharField(choices=[('MAL', 'Male'), ('FML', 'FeMale'), ('OTR', 'Other')], max_length=3, verbose_name='Gender')),
                ('nationality', models.CharField(max_length=50, verbose_name='Nationality')),
                ('mother_language', models.CharField(max_length=50, verbose_name='Mother Language')),
                ('other_languages', models.CharField(max_length=150, null=True, verbose_name='Other Languages')),
                ('english_status', models.CharField(choices=[('WEK', 'Weak'), ('GOD', 'Good'), ('EXT', 'Excellent')], max_length=3, verbose_name='English Status')),
                ('persian_status', models.CharField(choices=[('WEK', 'Weak'), ('GOD', 'Good'), ('EXT', 'Excellent')], max_length=3, verbose_name='Persian Status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
