# Generated by Django 4.1.5 on 2023-02-28 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0002_rename_usename_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='p_name',
        ),
        migrations.AlterModelTable(
            name='user',
            table='classapp_user',
        ),
    ]
