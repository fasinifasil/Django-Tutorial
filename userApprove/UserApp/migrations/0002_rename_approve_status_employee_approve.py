# Generated by Django 5.0 on 2023-12-13 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Approve_Status',
            new_name='approve',
        ),
    ]
