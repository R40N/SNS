# Generated by Django 4.2 on 2023-04-11 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_profile_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelTable(
            name='user',
            table='my_user',
        ),
    ]
