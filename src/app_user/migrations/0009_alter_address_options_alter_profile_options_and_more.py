# Generated by Django 4.2.2 on 2023-07-18 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0008_alter_address_postal_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ['-id'], 'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-id'], 'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-id'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
