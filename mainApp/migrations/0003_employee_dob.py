# Generated by Django 4.1.7 on 2023-06-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_remove_employee_dob_employee_email_employee_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dob',
            field=models.DateField(max_length=12, null=True),
        ),
    ]