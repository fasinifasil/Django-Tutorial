# Generated by Django 5.0 on 2023-12-16 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_leavereport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leavereport',
            old_name='EmployeeName',
            new_name='Emp_Name',
        ),
    ]