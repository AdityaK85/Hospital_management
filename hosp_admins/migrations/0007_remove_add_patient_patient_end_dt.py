# Generated by Django 4.1.7 on 2023-04-30 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosp_admins', '0006_doctor_dr_depart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_patient',
            name='patient_end_dt',
        ),
    ]
