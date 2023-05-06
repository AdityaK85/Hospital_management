# Generated by Django 4.1.7 on 2023-04-29 20:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosp_admins', '0004_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_patient',
            name='patient_start_dt',
            field=models.DateField(default=datetime.date(2023, 4, 30)),
        ),
        migrations.AlterField(
            model_name='hopsital_department',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_days', models.CharField(max_length=50)),
                ('available_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('per_patient_time', models.TimeField()),
                ('status', models.CharField(max_length=50)),
                ('fk_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosp_admins.departments')),
                ('fk_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosp_admins.doctor')),
            ],
        ),
    ]